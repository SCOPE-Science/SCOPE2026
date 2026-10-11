from itertools import combinations_with_replacement

def partitions(d,k):
    return (a for a in combinations_with_replacement(range(1,d-k+2),k) if sum(a)==d)

def h0_end(a):
    return sum(max(a[j]-a[i]+1,0) for i in range(len(a)) for j in range(len(a)))

def defect(a):
    return sum(max(a[i]-a[j]-1,0) for i in range(len(a)) for j in range(i))

def balanced(a):
    return a[-1]-a[0] <= 1

count=0
for k in range(2,7):
    for d in range(k,23):
        rows=[]
        for a in partitions(d,k):
            count += 1
            h0=h0_end(a)
            delta=defect(a)
            assert h0 == k*k + delta
            rows.append((h0+2,a,delta))
        minimum=min(row[0] for row in rows)
        maximum=max(row[0] for row in rows)
        q,s=divmod(d,k)
        balanced_type=(q,)*(k-s)+(q+1,)*s
        assert minimum == k*k+2
        assert [a for dim,a,delta in rows if dim==minimum] == [balanced_type]
        assert all((dim==minimum)==balanced(a) for dim,a,delta in rows)
        if d>=k+1:
            extreme=(1,)*(k-1)+(d-k+1,)
            assert maximum == (k-1)*d+3
            assert [a for dim,a,delta in rows if dim==maximum] == [extreme]

for a in range(1,50):
    for b in range(a,50):
        dim=h0_end((a,b))+2
        published_surface_dimension=6 if a==b else b-a+5
        assert dim == published_surface_dimension

print(f"VERIFY_OK partitions={count}; k=2..6, d=k..22; surface box 1<=a<=b<50")
