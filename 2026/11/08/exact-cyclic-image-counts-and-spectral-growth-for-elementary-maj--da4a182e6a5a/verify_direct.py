"""Independent direct enumeration of the synchronous Rule 232 image.

This script does not construct or use Boolean relation states.
"""

def direct_image(x, n):
    y = 0
    for i in range(n):
        left = (x >> ((i-1) % n)) & 1
        here = (x >> i) & 1
        right = (x >> ((i+1) % n)) & 1
        if left + here + right >= 2:
            y |= 1 << i
    return y


def recurrence(nmax):
    # D(z) = 1 -2z +2z^3 -2z^4 -2z^5 +3z^6 -2z^8 +z^10.
    d = [1,-2,0,2,-2,-2,3,0,-2,0,1]
    a = [0]*(nmax+1)
    for n in range(1,nmax+1):
        # Coefficients of -z D'(z), with zeros beyond degree ten.
        numerator = -n*d[n] if n < len(d) else 0
        a[n] = numerator - sum(d[k]*a[n-k]
                               for k in range(1,min(n,10)+1))
    return a


def main():
    predicted = recurrence(20)
    expected = [2,4,2,8,22,34,58,96,182,334,596,1046,1848,3308,5932,10608]
    assert predicted[1:17] == expected
    for n in range(1,17):
        actual = len({direct_image(x,n) for x in range(1<<n)})
        assert actual == predicted[n], (n,actual,predicted[n])
    print('DIRECT_ENUMERATION_PASS through_n=16')


if __name__ == '__main__':
    main()
