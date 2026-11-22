"""Exact independent checks for connected crossing spectra at fixed openers.

Python 3 standard library only; run: python verify.py
"""
from collections import defaultdict


def dyck_words(n):
    def visit(word, ups, downs):
        if len(word) == 2*n:
            yield word
            return
        if ups < n:
            yield from visit(word+'U', ups+1, downs)
        if downs < ups:
            yield from visit(word+'D', ups, downs+1)
    yield from visit('', 0, 0)


def primitive(word):
    h=0
    for s in word[:-1]:
        h += 1 if s=='U' else -1
        if h==0:
            return False
    return True


def all_matchings(word):
    def visit(pos, active, arcs):
        if pos==len(word):
            yield tuple(sorted(arcs))
        elif word[pos]=='U':
            yield from visit(pos+1,active+(pos,),arcs)
        else:
            for opener in active:
                yield from visit(pos+1,tuple(t for t in active if t!=opener),arcs+((opener,pos),))
    yield from visit(0,(),())


def crosses(edge1,edge2):
    a,b=edge1; c,d=edge2
    return a<c<b<d or c<a<d<b


def crossing_count(matching):
    return sum(crosses(matching[i],matching[j]) for i in range(len(matching)) for j in range(i))


def connected(matching):
    n=len(matching)
    seen={0};todo=[0]
    while todo:
        i=todo.pop()
        for j in range(n):
            if j not in seen and crosses(matching[i],matching[j]):
                seen.add(j);todo.append(j)
    return len(seen)==n


def height_max(word):
    h=0; result=0
    for s in word:
        if s=='U':h+=1
        else:result+=h-1;h-=1
    return result


def tree_construct(word):
    n=len(word)//2
    if n==1:
        return ((0,1),)
    cut=word.find('UD',1,len(word)-1)
    assert 0<cut<len(word)-2
    smaller=tree_construct(word[:cut]+word[cut+2:])
    lifted=[(a+2*(a>=cut),b+2*(b>=cut)) for a,b in smaller]
    spanning=[(a,b) for a,b in lifted if a<cut and b>cut+1]
    a,b=min(spanning,key=lambda z:z[1])
    lifted.remove((a,b))
    return tuple(sorted(lifted+[(a,cut+1),(cut,b)]))


def inversion_climb(matching):
    current=tuple(matching)
    while True:
        by_end=sorted(current,key=lambda e:e[1])
        for j in range(len(by_end)-1):
            (a,c),(b,d)=by_end[j:j+2]
            if a>b:
                replacement={(a,d),(b,c)}
                current=tuple(sorted((set(current)-{(a,c),(b,d)})|replacement))
                yield current
                break
        else:
            break


def main():
    sizes=defaultdict(int)
    states=0;swaps=0
    for n in range(1,7):
        for w in dyck_words(n):
            cs={crossing_count(M) for M in all_matchings(w) if connected(M)}
            want=set(range(n-1,height_max(w)+1)) if primitive(w) else set()
            assert cs==want,(w,cs,want)
            sizes[n]+=1
            if primitive(w):
                construction=tree_construct(w)
                assert connected(construction)
                assert crossing_count(construction)==n-1
                for M in all_matchings(w):
                    if not connected(M):continue
                    states+=1
                    last=crossing_count(M)
                    for new_M in inversion_climb(M):
                        assert connected(new_M),(w,M,new_M)
                        assert crossing_count(new_M)==last+1,(w,M,new_M,last)
                        last+=1;swaps+=1
                    assert last==height_max(w),(w,M,last)
        print('ALL_MATCHINGS_AND_SPECTRA_PASS',n,sizes[n])
    print('ALL_CONNECTED_BUBBLE_PATHS_PASS',states,swaps)
    for n in range(7,11):
        count=0
        for w in dyck_words(n):
            if not primitive(w):continue
            t=tree_construct(w)
            assert connected(t)
            assert crossing_count(t)==n-1
            c=last=n-1
            for next_t in inversion_climb(t):
                assert connected(next_t)
                assert crossing_count(next_t)==c+1
                c+=1
            assert c==height_max(w)
            count+=1
        print('INDUCTIVE_CONSTRUCTION_AND_INCREMENTAL_PATH_PASS',n,count)
    print('VERIFY_OK')

if __name__=='__main__':main()
