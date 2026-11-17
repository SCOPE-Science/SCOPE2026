"""Check the independent forest/ballot enumeration identity."""
from math import comb

def ballot_paths(speed, length):
    def walk(index,used):
        if index==length:
            return 1
        return sum(walk(index+1,used+u)
                   for u in range(speed*(index+1)-used))
    return walk(0,0)

def forest_coefficients(speed, max_degree):
    # Formal-power-series solution T=1+z*T^(speed+1), then T^speed.
    T=[1]+[0]*max_degree
    for degree in range(1,max_degree+1):
        a=[1]+[0]*(degree-1)
        for _ in range(speed+1):
            b=[0]*degree
            for k in range(degree):
                for j in range(degree-k):
                    b[k+j]+=a[k]*T[j]
            a=b
        T[degree]=a[degree-1]
    a=[1]+[0]*max_degree
    for _ in range(speed):
        b=[0]*(max_degree+1)
        for k in range(max_degree+1):
            for j in range(max_degree+1-k):
                b[k+j]+=a[k]*T[j]
        a=b
    return a

def run():
    tests=0
    for speed in range(1,6):
        coefs=forest_coefficients(speed,5)
        for length in range(0,6):
            cnt=ballot_paths(speed,length)
            formula=comb((speed+1)*(length+1)-2,length)//(length+1)
            assert cnt==coefs[length]==formula, (speed,length,cnt,coefs[length],formula)
            tests+=1
    print('independent ballot / forest / binomial checks:',tests)
    print('all exact coefficient identities: PASS')

if __name__=='__main__':run()
