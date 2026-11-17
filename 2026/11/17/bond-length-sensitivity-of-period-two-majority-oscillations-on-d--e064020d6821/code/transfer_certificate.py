"""Exact transfer calculation for synchronous majority on one-edge-defective squared cycles."""
import time

def make_matrices(alphabet=4):
    states=alphabet**4
    normal=[[] for _ in range(states)];d1_l=[[] for _ in range(states)];d1_r=[[] for _ in range(states)];d2_l=[[] for _ in range(states)];d2_r=[[] for _ in range(states)]
    for v in range(states):
        if alphabet==4:
            w=[(v>>(2*i))&3 for i in (3,2,1,0)]
        else: # diagonal pairs 00 and 11 represented by 0/1
            w=[(v>>i)&1 for i in (3,2,1,0)]
        for new in range(alphabet):
            a=w+[new]
            if alphabet==4:
                x=[p&1 for p in a];y=[p>>1 for p in a]
            else:x=y=a
            def med(c,vals):
                s=sum(vals); L=len(vals)
                return int(2*s>L) if 2*s!=L else c
            for target,off in ((normal,[-2,-1,1,2]),(d1_l,[-2,-1,2]),(d1_r,[-2,1,2]),(d2_l,[-2,-1,1]),(d2_r,[-1,1,2])):
                if med(x[2],[x[2+i] for i in off])==y[2] and med(y[2],[y[2+i] for i in off])==x[2]:
                    nxt=(v*alphabet+new)%states
                    target[v].append(nxt)
    return normal,d1_l,d1_r,d2_l,d2_r

def product_matrix(X,E):
    # input X is dense rows, E sparse adjacency rows
    order=len(X)
    dest=[[0]*order for _ in range(order)]
    for i,row in enumerate(X):
        out=dest[i]
        for j,targets in enumerate(E):
            z=row[j]
            if z:
                for k in targets:out[k]+=z
    return dest

def from_sparse(E):
    S=len(E);M=[[0]*S for _ in range(S)]
    for i,tar in enumerate(E):
        for j in tar:M[i][j]+=1
    return M

def calc(nmax=290):
    started=time.monotonic()
    answers={}
    for dist in (1,2):
        results={}
        for alphabet in (4,2):
            a,l1,r1,l2,r2=make_matrices(alphabet)
            if dist==1:
                M=product_matrix(from_sparse(l1),r1);offset=2
            else:
                M=product_matrix(product_matrix(from_sparse(l2),a),r2);offset=3
            # For n=offset, trace M; n increases by one at every multiply by a.
            for n in range(offset,nmax+1):
                if n>=7:results.setdefault(n,{})[alphabet]=sum(M[i][i] for i in range(len(M)))
                if n!=nmax:M=product_matrix(M,a)
        for n,counts in results.items():
            P=counts[4];H=counts[2]
            assert (P-H)>=0 and (P-H)%2==0,(dist,n,P,H)
            C=(P-H)//2
            predicted=2*(n%4==0)+2*(n%6==0)+(dist==2 and n%4==3)
            if C!=predicted:raise AssertionError((dist,n,C,predicted,P,H))
        answers[dist]=[results[n][4]-results[n][2] for n in range(7,nmax+1)]
        # The first 272 differences annihilate the entire sequence by Cayley--Hamilton.
        assert len(answers[dist]) >= 284
        for j in range(272):
            assert answers[dist][j+12]==answers[dist][j], (dist,j)
        print('dist',dist,'checked n=7..',nmax,'all exact; max numerator',answers[dist][-1],'elapsed',round(time.monotonic()-started,1),flush=True)
    print('CAYLEY_HAMILTON_CERTIFIED: 12-periodic exact formula extends to ALL n >=7, since difference of traces of 256-state and 16-state matrix powers obeys 272nd-order recurrence; consecutive zeros of D(n+12)-D(n) for n=7..278 established.',flush=True)
if __name__=='__main__':calc()
