"""Independent digital recurrence and extremal-defect checks."""
limit = 4**7

def bit(i):
    x = i + 1
    exponent = (x & -x).bit_length() - 1
    return exponent % 2

bits = [bit(i) for i in range(2*limit)]
for i in range(limit):
    assert bits[2*i] == 0
    assert bits[2*i+1] == 1-bits[i]

prefix = [0]*(2*limit+1)
for i, b in enumerate(bits):
    prefix[i+1] = prefix[i] + b

mins = [0]*(limit+1)
maxs = [0]*(limit+1)
maxs[1] = 1
D = [0]*(limit+1)
for n in range(1, limit+1):
    assert prefix[n] == n//2-prefix[n//2]
    if n > 1:
        k = n//2
        if n%2 == 0:
            mins[n] = k-maxs[k]
            maxs[n] = k-mins[k]
        else:
            mins[n] = k-maxs[k]
            maxs[n] = k+1-mins[k+1]
    D[n] = maxs[n]-prefix[n]
for t in range((limit-3)//4+1):
    assert D[4*t] == D[t]
    assert D[4*t+1] == D[t]+1
    assert D[4*t+2] == D[t]
    assert D[4*t+3] == D[t+1]+bits[t]
for j in range(1,8):
    n=(4**j-1)//3
    assert D[n] == j
    assert mins[n] == prefix[n]
    assert maxs[n] == prefix[2*n]-prefix[n]
    assert max(D[1:4**j]) == j
print('DIGITAL_OK length',limit,'sharp envelope j=1..7; all four recurrence cases checked')
