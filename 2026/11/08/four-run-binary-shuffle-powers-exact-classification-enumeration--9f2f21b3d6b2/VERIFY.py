"""Independent checks for the four-run equal-subsequence partition theorem."""
from functools import lru_cache
from itertools import product


def exact_characterization(q, a, b, c, d):
    if (a+c)%q or (b+d)%q:
        return False
    A=(a+c)//q
    B=(b+d)//q
    return (all(t%q==0 for t in (a,b,c,d))
            or ((b+B-1)//B <= a//A))


def independent_search(q,a,b,c,d):
    word='0'*a+'1'*b+'0'*c+'1'*d
    if len(word)%q or (a+c)%q or (b+d)%q:
        return False
    target=len(word)//q
    states={tuple(['']*q)}
    for letter in word:
        nxt=set()
        for state in states:
            for j in range(q):
                if len(state[j])>=target:
                    continue
                x=list(state)
                x[j]+=letter
                t=max(x,key=len)
                if all(t.startswith(z) for z in x):
                    nxt.add(tuple(sorted(x)))
        states=nxt
        if not states:
            return False
    return any(len(set(st))==1 for st in states)


def exact_count(q,A,B):
    P=q*(q-1)*A*B//2
    E=(A-1)*(B-1)
    J=sum((B*(q*alpha//A))//q for alpha in range(1,A))
    return P+E-J


def count_by_classes(q,A,B):
    return sum(exact_characterization(q,a,b,q*A-a,q*B-b)
               for a in range(1,q*A) for b in range(1,q*B))


def run():
    checked=0
    for q in (2,3,4):
        for a,b,c,d in product(range(1,6),repeat=4):
            if (a+c)%q or (b+d)%q or a+b+c+d>20:
                continue
            predicted=exact_characterization(q,a,b,c,d)
            actual=independent_search(q,a,b,c,d)
            assert predicted==actual,(q,a,b,c,d,predicted,actual)
            checked+=1
    counted=0
    for q in range(2,9):
        for A in range(1,15):
            for B in range(1,15):
                predicted=exact_count(q,A,B)
                observed=count_by_classes(q,A,B)
                assert predicted==observed,(q,A,B,predicted,observed)
                counted+=1
    print('direct-shuffle dynamic-search comparisons:',checked)
    print('composition-count comparisons:',counted)
    for q in range(2,8):
        N=1000
        observed=exact_count(q,N,N)/((q*N-1)*(q*N-1))
        limiting=(q**3-q**2+q+1)/(2*q**3)
        assert abs(observed-limiting)<.005,(q,observed,limiting)
        print(f'limit q={q}: sample={observed:.7f}, predicted={limiting:.7f}')
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    run()
