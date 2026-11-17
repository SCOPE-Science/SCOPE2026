"""Exact binary wheel adjacency iteration and independent functional-graph census."""
from collections import deque, Counter


def wheel_rows(n):
    assert n >= 3
    rows = [(sum(1 << (i+1) for i in range(n)))]
    for i in range(n):
        rows.append(1 | (1 << (1+(i-1)%n)) | (1 << (1+(i+1)%n)))
    return rows


def matmul(A, B):
    return [reduce_row(row, B) for row in A]


def reduce_row(row, B):
    out = 0
    while row:
        bit = row & -row
        out ^= B[bit.bit_length()-1]
        row ^= bit
    return out


def rank(R):
    basis = {}
    for v in R:
        while v:
            k = v.bit_length()-1
            if k in basis: v ^= basis[k]
            else:
                basis[k] = v
                break
    return len(basis)


def jordan_parts(n):
    h = n & -n
    if h == 1: return []
    if h == 2: return [3]
    if h == 4: return [3,1,1]
    return [h//2, h//2, 1]


def predicted_nullity(n, t):
    return sum(min(t, k) for k in jordan_parts(n))


def census(n):
    rows = wheel_rows(n)
    N = 1 << (n+1)
    succ = [reduce_row(v,rows) for v in range(N)]
    indegree = [0]*N
    for w in succ: indegree[w] += 1
    q = deque(i for i,d in enumerate(indegree) if d==0)
    peeled=[]
    while q:
        v = q.popleft()
        peeled.append(v)
        w=succ[v]
        indegree[w]-=1
        if indegree[w]==0: q.append(w)
    dist = [0]*N
    for v in reversed(peeled): dist[v] = dist[succ[v]]+1
    actual = Counter(dist)
    h = n & -n
    stable = (n+1 if h==1 else n-h)
    max_t = max(jordan_parts(n),default=0)
    expected = Counter({0:1<<stable})
    for t in range(1,max_t+1):
        expected[t] = (1 << (stable+predicted_nullity(n,t))) - (1 << (stable+predicted_nullity(n,t-1)))
    assert actual == expected,(n,actual,expected)
    return actual, len(peeled)


def main():
    comparisons=0
    for n in list(range(3,101))+[120,128,160,192,256]:
        A = wheel_rows(n)
        power = [1<<i for i in range(n+1)]
        max_t=max(jordan_parts(n),default=0)
        for t in range(1,max_t+3):
            power=matmul(power,A)
            nullity=n+1-rank(power)
            prediction=predicted_nullity(n,t)
            assert nullity==prediction,(n,t,nullity,prediction)
            comparisons+=1
    states=0
    for n in range(3,17):
        actual,_=census(n)
        states += 1<<(n+1)
        print('census',n,sorted(actual.items()))
    print('WHEEL_MATRIX_OK', 'power_rank_comparisons',comparisons, 'exhaustive_states',states)

if __name__=='__main__': main()
