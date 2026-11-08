"""Separate direct triple-enumeration boundary check; no dynamic programming."""
checked = 0
for q in range(3,18):
    for k in range(2,18):
        a=q*k
        b=a+1
        c=a+q
        d=min(q-1,k+1)
        f1=a*(k+q-2+d)-1
        f0=a*(k+q-2)-1
        def count(n):
            result=0
            for x in range(n//a+1):
                m=n-a*x
                for y in range(m//b+1):
                    if (m-b*y)%c==0: result+=1
            return result
        assert count(f0)==0, (q,k,'f0')
        assert count(f1)==1, (q,k,'f1')
        assert count(f1+1)>=2, (q,k,'f1+1')
        checked+=1
print(f'PASS direct_triple_enumeration_parameter_pairs={checked} tested_boundaries=3')
