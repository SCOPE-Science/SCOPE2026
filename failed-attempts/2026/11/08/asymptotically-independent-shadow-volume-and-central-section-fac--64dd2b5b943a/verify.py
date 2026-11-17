"""Supplementary finite-dimensional checks for regular-simplex shadow/section laws.

Requires Python 3, NumPy and SciPy. This script tests formulas; it does not
replace the asymptotic proof.
"""
import itertools
import math
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from scipy.special import gammaln


def projection_statistic(u):
    u = np.asarray(u, dtype=float)
    N = len(u)
    u = u-u.mean()
    u = u/np.linalg.norm(u)
    return np.sum(np.abs(u))/np.sqrt(N)


def formula_mean(N):
    return math.sqrt(N-1)*math.exp(gammaln((N-1)/2)-gammaln(N/2))/math.sqrt(math.pi)


def formula_second_moment(N):
    r = -1/(N-1)
    return 1/N + 2*(N-1)/(math.pi*N)*(math.sqrt(1-r*r)+r*math.asin(r))


def formula_section_mean(N):
    return 0.25+(N-1)/(2*math.pi)*math.asin(-1/(N-1))


def section_vector(u):
    a = np.asarray(u)-np.mean(u)
    N = len(a)
    K = int(np.sum(a>0))
    return [math.comb(N,j)-math.comb(K,j)-math.comb(N-K,j)
            for j in range(2,N)]


def direct_section_face_vector(u):
    a = np.asarray(u)-np.mean(u)
    N=len(a)
    vals=[]
    for j in range(2,N):
        vals.append(sum(bool(np.any(a[list(S)]>0) and np.any(a[list(S)]<0))
                        for S in itertools.combinations(range(N),j)))
    return vals


def direct_projection(u):
    a=np.asarray(u, dtype=float)
    N=len(a)
    a-=a.mean()
    a/=np.linalg.norm(a)
    basis=null_space(np.column_stack((np.ones(N),a)).T)
    verts=basis.T
    if N==3:
        measured=float(np.ptp(verts))
    else:
        measured=ConvexHull(verts.T).volume
    claimed=math.sqrt(N)/(2*math.factorial(N-2))*sum(abs(a))
    return measured,claimed


def check():
    rng=np.random.default_rng(76214)
    count=0
    for N in range(3,9):
        for _ in range(30):
            g=rng.standard_normal(N)
            a,b=direct_projection(g)
            assert abs(a-b)<5e-9, (N,a,b)
            assert section_vector(g)==direct_section_face_vector(g)
            count+=2
    for N in [3,4,5,8,16,50,150]:
        draws=150000 if N<=16 else 60000
        g=rng.standard_normal((draws,N))
        a=g-g.mean(axis=1)[:,None]
        theta=a/np.linalg.norm(a,axis=1)[:,None]
        X=np.sum(np.abs(theta),axis=1)/math.sqrt(N)
        S=(a>0).sum(axis=1)-(a<0).sum(axis=1)
        Y=S**2/(4*N)
        assert abs(X.mean()-formula_mean(N)) < 0.01
        assert abs(np.mean(X**2)-formula_second_moment(N)) < 0.02
        assert abs(Y.mean()-formula_section_mean(N)) < 0.035
        count+=3
    for N in [200,1000]:
        XX=[]; TT=[]
        for _ in range(15):
            g=rng.standard_normal((500,N))
            a=g-g.mean(axis=1)[:,None]
            X=np.sum(np.abs(a),axis=1)/np.linalg.norm(a,axis=1)/math.sqrt(N)
            S=(a>0).sum(axis=1)-(a<0).sum(axis=1)
            XX.append(np.sqrt(N)*(X-math.sqrt(2/math.pi)))
            TT.append(S/np.sqrt(N))
        XX=np.concatenate(XX); TT=np.concatenate(TT)
        cv=np.cov(XX,TT)
        target_x=1-3/math.pi
        target_t=1-2/math.pi
        assert abs(cv[0,0]-target_x)<0.018,(N,cv[0,0],target_x)
        assert abs(cv[1,1]-target_t)<0.050,(N,cv[1,1],target_t)
        assert abs(cv[0,1])<0.035,(N,cv[0,1])
        count+=3
        print('CLT N',N, 'observed cov',cv.tolist(), 'targets',target_x,target_t)
    print('PASS',count,'finite checks; exact mean and variance and geometry corroborated')


if __name__=='__main__':
    check()
