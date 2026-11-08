"""Exact three-cohort products and Markov parity-3 covariance checks (Python 3)."""
from fractions import Fraction as Q
from itertools import product
import math

def main():
    checks=0
    cases=[((Q(4),Q(8)),(Q(1,2),Q(1,4)),(Q(1,2),Q(1,2))),((Q(3),Q(5)),(Q(1,2),Q(2,3)),(Q(2,3),Q(3,4)))]
    for f,s,t in cases:
        for n in (3,6,9,12):
            for seq in product((0,1),repeat=n):
                a,b,c=Q(2),Q(3),Q(5)
                for e in seq:a,b,c=f[e]*c,s[e]*a,t[e]*b
                aa,bb,cc=Q(2),Q(3),Q(5)
                for j in range(0,n,3):
                    aa*=f[seq[j+2]]*t[seq[j+1]]*s[seq[j]]
                    bb*=s[seq[j+2]]*f[seq[j+1]]*t[seq[j]]
                    cc*=t[seq[j+2]]*s[seq[j+1]]*f[seq[j]]
                assert (a,b,c)==(aa,bb,cc)
                checks+=1
    a=Q(1,4);b=Q(1,2);P=((1-a,a),(b,1-b));pi=(b/(a+b),a/(a+b));theta=1-a-b
    for n in (3,6,9):
        u=Q(2);v=Q(-3);w=Q(1)
        coeff=((u,v,w),(v,w,u),(w,u,v))
        coeff=tuple(tuple(x-(u+v+w)/3 for x in row) for row in coeff)
        esum=[[Q(0) for _ in range(3)]for _ in range(3)]
        for seq in product((0,1),repeat=n):
            pr=pi[seq[0]]
            for k in range(1,n):pr*=P[seq[k-1]][seq[k]]
            h=[Q(x)-pi[1] for x in seq]
            X=[sum(coeff[i][t%3]*h[t] for t in range(n))for i in range(3)]
            for i in range(3):
                for j in range(3):esum[i][j]+=pr*X[i]*X[j]
        for i in range(3):
            for j in range(3):
                pred=pi[0]*pi[1]*sum(coeff[i][t%3]*coeff[j][s%3]*theta**abs(t-s) for t in range(n) for s in range(n))
                assert esum[i][j]==pred
                checks+=1
    print('PASS',checks,'exact rational checks; expected triangular extreme mean',3*math.sqrt(3)/(2*math.sqrt(2*math.pi)))
if __name__=='__main__':main()
