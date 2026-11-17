"""Independent exhaustive update check on C_n Cartesian K_3.

Uses Python standard library only. Counts fixed labelled 0-1 colourings.
"""

def fixed(mask, n):
    columns = [(mask >> (3*i)) & 7 for i in range(n)]
    for i in range(n):
        a, b, c = columns[(i-1) % n], columns[i], columns[(i+1) % n]
        for r in range(3):
            side = ((a >> r)&1) + ((c >> r)&1)
            inner = ((b >> ((r+1)%3))&1) + ((b >> ((r+2)%3))&1)
            ones = side + inner
            if ((b>>r)&1) != int(ones >= (2 if (b>>r)&1 else 3)):
                return False
    return True

expected = {3:32,4:94,5:218,6:712,7:2234}
for n in range(3, 8):
    count = sum(fixed(mask,n) for mask in range(1<<(3*n)))
    assert count == expected[n], (n,count,expected[n])
    print(f'{n}: {count}, tested {1 << (3*n)} states')
print('DIRECT_UPDATE_OK')
