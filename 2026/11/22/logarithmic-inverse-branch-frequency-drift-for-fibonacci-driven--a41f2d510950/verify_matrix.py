"""Exact eight-letter substitution certificate for Fibonacci-driven Rule 150."""

def step(s, digit):
    a, b = s >> 1, s & 1
    return 2*b + (a ^ b ^ digit)

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def rowmul(r,A):
    return [sum(r[i]*A[i][j] for i in range(len(r))) for j in range(len(r))]

def main():
    w0, w1 = '0','1'
    for _ in range(16):
        w0,w1=w0+w1,w0
    assert (len(w0),len(w1))==(2584,1597)
    M=[[0]*8 for _ in range(8)]
    for letter, word in enumerate((w0,w1)):
        for s in range(4):
            q=s
            for ch in word:
                d=int(ch)
                M[4*d+q][4*letter+s]+=1
                q=step(q,d)
            assert q==step(s,letter), (letter,s,q)
    expected=[[400,399,402,396,249,244,247,247],
              [399,400,400,398,247,246,247,247],
              [399,399,395,404,244,251,246,246],
              [399,399,400,399,247,246,247,247],
              [246,246,249,246,154,150,153,153],
              [246,246,243,252,150,156,152,152],
              [246,246,249,246,153,150,154,153],
              [249,249,246,243,153,154,151,152]]
    assert M==expected
    R=[3,-1,-1,-1,3,-1,-1,-1]
    R1=rowmul(R,M)
    R2=rowmul(R1,M)
    R3=rowmul(R2,M)
    V=[R3[i]-R[i] for i in range(8)]
    assert V==[0,0,24,-24,24,-24,0,0]
    assert rowmul(V,M)==V
    assert [R[:4],R1[:4],R2[:4]]==[[3,-1,-1,-1],[0,-4,20,-16],[9,5,17,-31]]
    print('PASS: exact substitution matrix, return permutations, initial data, and universal recurrence')
if __name__=='__main__':main()
