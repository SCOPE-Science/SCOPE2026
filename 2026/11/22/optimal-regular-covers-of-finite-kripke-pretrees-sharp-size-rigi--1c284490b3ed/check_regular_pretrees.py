"""Finite checks for optimal bounded-morphic regularizations of rooted pretrees.
Standard library only. All large-parameter claims rely on the written proof.
"""
from itertools import product
from collections import defaultdict
from math import factorial, comb
from functools import lru_cache


def rooted_shapes(n):
    @lru_cache(None)
    def shapes(t):
        if t == 1:
            return ((),)
        types = [(j, x) for j in range(1, t) for x in shapes(j)]
        types.sort(key=lambda z:(z[0],repr(z[1])))
        out = set()
        def rec(rem, start, acc):
            if rem == 0:
                out.add(tuple(acc)); return
            for i in range(start, len(types)):
                j,x = types[i]
                if j > rem: break
                rec(rem-j,i,acc+[x])
        rec(t-1,0,[])
        return tuple(sorted(out,key=repr))
    return shapes(n)


def parent_from_shape(shape):
    parent=[-1]
    def visit(s, p):
        for sub in s:
            q=len(parent)
            parent.append(p)
            visit(sub,q)
    visit(shape,0)
    return tuple(parent)


def children(p):
    ch=[[] for _ in p]
    for i,a in enumerate(p):
        if i: ch[a].append(i)
    return ch


def descendants(p):
    ch=children(p)
    return [set([i]).union(*(z for z in [])) if False else {i} | set().union(*(descendants_from(ch,j) for j in ch[i])) for i in range(len(p))]


def descendants_from(ch,i):
    return {i} | set().union(*(descendants_from(ch,j) for j in ch[i]))


def make_optimal_source(p,k):
    ch=children(p)
    leaves=[i for i,z in enumerate(ch) if not z]
    out_p=[-1]
    images=[0]
    def fill(t, s):
        for u in ch[t]:
            i=len(out_p);out_p.append(s);images.append(u)
            fill(u,i)
        if ch[t]:
            leaf=next(x for x in leaves if x in descendants_from(ch,t))
            for _ in range(k-len(ch[t])):
                out_p.append(s);images.append(leaf)
    fill(0,0)
    return tuple(out_p),tuple(images)


def is_pmorphism(sp,tp,fn):
    sch,tch=children(sp),children(tp)
    td=[descendants_from(tch,i) for i in range(len(tp))]
    for s in range(len(sp)):
        if {fn[u] for u in descendants_from(sch,s)} != td[fn[s]]:
            return False
    return True


def aut_internal(p):
    ch=children(p)
    if not ch[0]: return 1
    def recurse(i):
        kids=[j for j in ch[i] if ch[j]]
        counts=defaultdict(int)
        a=1
        for j in kids:
            sh,b=recurse(j)
            counts[sh]+=1; a*=b
        for count in counts.values(): a*=factorial(count)
        return tuple(sorted(((sh,count) for sh,count in counts.items()),key=repr)),a
    return recurse(0)[1]


def onto(m,c):
    return sum((-1)**j*comb(c,j)*(c-j)**m for j in range(c+1))


def formula(p,k,m,sizes):
    ch=children(p)
    if not ch[0]:return onto(m,sizes[0])
    val=aut_internal(p)
    for t in range(len(p)):
        if not ch[t]:continue
        u=sum(bool(ch[v]) for v in ch[t])
        b=[v for v in ch[t] if not ch[v]]
        leaf=[v for v in descendants_from(ch,t) if not ch[v]]
        q=k-u
        wt={v:onto(m,sizes[v]) for v in leaf}
        W=0
        for mask in range(1<<len(b)):
            forbidden={v for i,v in enumerate(b) if mask>>i&1}
            W+= (-1)**len(forbidden)*(sum(wt[v] for v in leaf if v not in forbidden)**q)
        val*=onto(m,sizes[t])*W
    return val


def check_cluster_map(sp,tp,sizes,m,fn):
    # fn gives one target (cluster, element) for every source (cluster, element)
    sc=children(sp);tc=children(tp)
    source_succ=[descendants_from(sc,i) for i in range(len(sp))]
    target_succ=[descendants_from(tc,i) for i in range(len(tp))]
    for i in range(len(sp)):
        actual={fn[j*m+b] for j in source_succ[i] for b in range(m)}
        for a in range(m):
            t,which=fn[i*m+a]
            expected={(v,b) for v in target_succ[t] for b in range(sizes[v])}
            if actual!=expected: return False
    return True


def brute_regular(sp,tp,sizes,m):
    target=[(t,a) for t,c in enumerate(sizes) for a in range(c)]
    root=target[:sizes[0]]
    cnt=0
    # Every source cluster must map into one target cluster; enumerate target cluster choices, then its individual maps.
    for cluster_images in product(range(len(tp)),repeat=len(sp)-1):
        allimages=(0,)+cluster_images
        # Order preservation at quotient level is an inexpensive rejection.
        tc=children(tp); sc=children(sp)
        if any(allimages[j] not in descendants_from(tc,allimages[i]) for i in range(len(sp)) for j in sc[i]):
            continue
        target_cluster_choices=[[tuple((t,a) for a in tup) for tup in product(range(sizes[t]),repeat=m)] for t in allimages]
        for choices in product(*target_cluster_choices):
            flat=sum((list(x) for x in choices),[])
            if check_cluster_map(sp,tp,sizes,m,flat):cnt+=1
    return cnt


@lru_cache(None)
def full_shapes(k,internal):
    if internal==0:return ((),)
    parts=full_shapes
    out=set()
    options=[(j,z) for j in range(internal) for z in parts(k,j)]
    options.sort(key=lambda a:(a[0],repr(a[1])))
    def rec(left,start,children):
        if len(children)==k:
            if left==0:out.add(tuple(sorted(children,key=repr)))
            return
        for i in range(start,len(options)):
            j,z=options[i]
            if j>left:break
            rec(left-j,i,children+[z])
    rec(internal-1,0,[])
    return tuple(sorted(out,key=repr))

@lru_cache(None)
def exists_pmorph_shape(src,target):
    if not target: return True
    if not src: return False
    if any(exists_pmorph_shape(c,target) for c in src):return True
    if len(target)>len(src):return False
    return any(all(exists_pmorph_shape(src[i],target[j]) for j,i in enumerate(indices))
               for indices in __import__('itertools').permutations(range(len(src)),len(target)))


def shape_of_tree(p):
    ch=children(p)
    def rec(i):return tuple(sorted((rec(j) for j in ch[i]),key=repr))
    return rec(0)


def check_optimal_shape_rigidity():
    tested=0
    for n in range(1,8):
        for target in rooted_shapes(n):
            tp=parent_from_shape(target)
            I=sum(bool(z) for z in children(tp))
            if I>4:continue
            d=max(map(len,children(tp)))
            for k in range(max(1,d),min(3,max(1,d)+1)+1):
                if k<d:continue
                source,_=make_optimal_source(tp,k)
                optimal=shape_of_tree(source)
                for i in range(max(0,I-1),I+1):
                    for candidate in full_shapes(k,i):
                        possible=exists_pmorph_shape(candidate,target)
                        assert possible == (i==I and candidate==optimal),(n,k,target,i,candidate,optimal)
                        tested+=1
    return tested

def check_branch_obstruction():
    checks=0
    for n in range(3,7):
        for target in rooted_shapes(n):
            deg=max(map(len,children(parent_from_shape(target))))
            if deg<=1: continue
            for k in range(1,deg):
                if k>2:continue
                for i in range(5):
                    for src in full_shapes(k,i):
                        assert not exists_pmorph_shape(src,target),(src,target)
                        checks+=1
    return checks

def main():
    tested=0
    brute=0
    for n in range(1,7):
        for shape in rooted_shapes(n):
            p=parent_from_shape(shape)
            ch=children(p)
            I=sum(bool(a) for a in ch)
            d=max(map(len,ch))
            for k in range(max(1,d),min(3,max(1,d)+1)+1):
                if k<d:continue
                sp,images=make_optimal_source(p,k)
                assert sum(bool(a) for a in children(sp))==I
                assert len(sp)==1+k*I
                assert is_pmorphism(sp,p,images)
                # For small canonical source, brute-count all vertex maps directly.
                if len(sp)<=7 and n<=5:
                    actual=0
                    for target_tail in product(range(n),repeat=len(sp)-1):
                        if is_pmorphism(sp,p,(0,)+target_tail):actual+=1
                    expected=formula(p,k,1,[1]*n)
                    assert actual==expected,(p,k,actual,expected)
                    brute+=1
                tested+=1
    # Test nontrivial target clusters via brute enumeration, including pointed counts.
    cluster_cases=[((-1,),1,2,(2,)),((-1,0,0),2,2,(2,1,2)),((-1,0,1),2,2,(1,2,2)),((-1,0,0),3,2,(1,2,2)),((-1,0,1),2,1,(1,1,1))]
    cluster_tested=0
    for p,k,m,sizes in cluster_cases:
        sp,images=make_optimal_source(p,k)
        if len(sp)*m > 9: continue
        count=brute_regular(sp,p,sizes,m)
        wanted=formula(p,k,m,sizes)
        assert count==wanted,(p,k,m,sizes,count,wanted)
        cluster_tested+=1
    print('VERIFY_OK shapes',tested,'brute_tree_counts',brute,'cluster_brute',cluster_tested,'shape_rigidity',check_optimal_shape_rigidity(),'branch_obstruction',check_branch_obstruction())

if __name__=='__main__': main()
