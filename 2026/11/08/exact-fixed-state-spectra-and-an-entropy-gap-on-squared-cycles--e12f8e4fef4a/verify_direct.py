"""Independent direct synchronous-update enumeration for C_n squared."""

def count(n, minority):
    found = 0
    for state in range(1 << n):
        stable = True
        for i in range(n):
            bit = (state >> i) & 1
            near = ((state >> ((i-2) % n)) & 1, (state >> ((i-1) % n)) & 1,
                    (state >> ((i+1) % n)) & 1, (state >> ((i+2) % n)) & 1)
            same = sum(v == bit for v in near)
            if (same > 2 if minority else same < 2):
                stable = False
                break
        found += stable
    return found

def transfer(minority):
    T = [[0]*16 for _ in range(16)]
    for k in range(16):
        b = [(k>>j)&1 for j in (3,2,1,0)]
        for c in (0,1):
            same = sum(v == b[2] for v in (b[0],b[1],b[3],c))
            if (same <= 2 if minority else same >= 2):
                T[k][(2*k+c)%16] += 1
    return T

def matmul(A,B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

for mode in (True, False):
    T=transfer(mode)
    P=[row[:] for row in T]
    print('mode', 'minority' if mode else 'majority')
    for n in range(1,17):
        if n>=5:
            direct = count(n,mode)
            trace = sum(P[k][k] for k in range(16))
            assert direct == trace, (n,direct,trace)
            print(n,direct)
        if n<16: P = matmul(P,T)
print('VERIFY_DIRECT_OK')
