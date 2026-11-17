"""Independent original-rule evolution on all labelled rings of sizes 3..16."""

def update(x,n):
    y=0
    for i in range(n):
        a=(x>>((i-1)%n))&1
        b=(x>>i)&1
        c=(x>>((i+1)%n))&1
        y|=((54>>(4*a+2*b+c))&1)<<i
    return y

for n in range(3,17):
    counts={1:0,2:0,3:0,6:0}
    six_states=[]
    for x in range(1<<n):
        y=x
        for t in range(1,7):
            y=update(y,n)
            if t in counts and y==x:
                counts[t]+=1
    # Inclusion-exclusion for least period 6.
    p6=counts[6]-counts[2]-counts[3]+counts[1]
    expected=24 if n%8==0 else 0
    assert counts[1]==1
    assert counts[3]==1
    assert counts[2]==1+(4 if n%4==0 else 0)
    assert counts[6]==1+(4 if n%4==0 else 0)+expected
    assert p6==expected
    if expected:
        for x in range(1<<n):
            y=x
            for _ in range(3): y=update(y,n)
            z=y
            for _ in range(3): z=update(z,n)
            if z==x and y!=x and update(update(x,n),n)!=x:
                six_states.append(x)
                assert y==(((x<<4)|(x>>(n-4)))&((1<<n)-1))
        assert len(six_states)==24
    print(f'n={n:2d} Fix1={counts[1]} Fix2={counts[2]} Fix3={counts[3]} Fix6={counts[6]} least6={p6}')
print('PASS independent direct-state enumeration n=3..16; all six-cycles obey half-period four-site shift')
