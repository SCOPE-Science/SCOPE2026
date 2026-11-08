"""Independent finite-field image checks for the square map on UT_5.
Run: python3 verify_squares.py. Only the Python standard library is needed.
"""
from itertools import product
from collections import Counter


def mul(a, b, q):
    if q == 2:
        return a & b
    if q == 4:
        # F4 = F2[z]/(z^2+z+1), encoded by 0,1,z,z+1.
        t = 0
        for bit in (0, 1):
            if (b >> bit) & 1:
                t ^= a << bit
        if t & 8:
            t ^= 0b1110  # reduce z^3=z^2+z by z^2+z+1
        if t & 4:
            t ^= 0b111  # reduce z^2=z+1
        return t
    raise ValueError("q must be 2 or 4")


def square_coordinates(entries, q):
    """Compute (I+N)^2 by literal 5-by-5 matrix multiplication."""
    indices = ((0,1),(1,2),(2,3),(3,4),(0,2),(1,3),(2,4),(0,3),(1,4),(0,4))
    N = [[0]*5 for _ in range(5)]
    for (i,j),val in zip(indices,entries):
        N[i][j] = val
    out=[]
    for i,j in ((0,2),(1,3),(2,4),(0,3),(1,4),(0,4)):
        s=0
        for t in range(i+1,j):
            s ^= mul(N[i][t],N[t][j],q)
        out.append(s)
    return tuple(out)


def predicts(u,v,w,x,y,z,q):
    if v==0:
        return mul(u,w,q)==0
    if u==0 and w==0:
        return mul(v,z,q)==mul(x,y,q)
    return True


def predicted_fiber(u,v,w,x,y,z,q):
    if v:
        if u or w:
            return q**3*(q-1)
        return q**4*(q-1) if mul(v,z,q)==mul(x,y,q) else 0
    if u and w:
        return 0
    if u or w:
        return q**4*(q-1)
    if x and y:
        return q**4*(q-1)
    if x or y:
        return q**4*(q*q-1)
    if z:
        return 3*q**5*(q-1)
    return q**5*(5*q-4)


def check(q):
    hist=Counter()
    for c in product(range(q),repeat=9):
        # The (1,5) input entry does not enter the square, so fix it at zero.
        out=square_coordinates(c+(0,),q)
        hist[out]+=q # restore all q free values of the top-right input entry
    actual=set(hist)
    predicted={a for a in product(range(q),repeat=6) if predicts(*a,q)}
    assert actual==predicted, (q,len(actual-predicted),len(predicted-actual))
    for a in product(range(q),repeat=6):
        assert hist[a]==predicted_fiber(*a,q), (q,a,hist[a],predicted_fiber(*a,q))
    n_expected=q**6-q**5+q**4+q**3-q**2
    assert len(actual)==n_expected,(q,len(actual),n_expected)
    assert sum(hist.values())==q**10
    assert all(v%q==0 for v in hist.values())
    print(f'q={q} field={"F2" if q==2 else "F4"} inputs={q**10} image={len(actual)} inaccessible={q**6-len(actual)} field_and_fiber_checks=PASS')


def check_unclosed():
    # (I+E13) and (I+E35) are each squares; their product has u=w=1,v=0.
    one=(1,0,0,0,0,0)
    two=(0,0,1,0,0,0)
    assert predicts(*one,2) and predicts(*two,2)
    assert not predicts(1,0,1,0,0,1,2)
    print('nonclosure_witness=PASS')

if __name__=='__main__':
    check(2)
    check(4)
    check_unclosed()
    print('ALL_UNITRIANGULAR_SQUARE_IMAGE_CHECKS_PASS')
