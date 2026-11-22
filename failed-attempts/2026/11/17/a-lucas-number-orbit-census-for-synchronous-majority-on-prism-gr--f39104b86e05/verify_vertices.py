"""Independent exhaustive bitset update of synchronous majority on prism graphs."""

def update(state, n):
    mask = (1 << n) - 1
    top = state & mask
    bottom = (state >> n) & mask
    top_left = ((top << 1) & mask) | (top >> (n-1))
    top_right = (top >> 1) | ((top & 1) << (n-1))
    bottom_left = ((bottom << 1) & mask) | (bottom >> (n-1))
    bottom_right = (bottom >> 1) | ((bottom & 1) << (n-1))
    next_top = (top_left & top_right) | (top_left & bottom) | (top_right & bottom)
    next_bottom = ((bottom_left & bottom_right) | (bottom_left & top) |
                   (bottom_right & top))
    return next_top | (next_bottom << n)


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def formula(n):
    l, ll = lucas(n), lucas(2*n)
    if n % 6 == 0:
        return l + 4, ll + 8*l + 18
    if n % 6 in (2,4):
        return l + 1, ll + 2*l + 3
    if n % 6 == 3:
        return l, ll + 4
    return l + 3, ll + 1

for n in range(3, 11):
    count1 = count2 = 0
    for state in range(1 << (2*n)):
        image = update(state,n)
        if image == state:
            count1 += 1
        if update(image,n) == state:
            count2 += 1
    assert (count1, count2) == formula(n), (n,count1,count2,formula(n))
    print(f'n={n}: {1<<(2*n)} states, fixed={count1}, period-dividing-two={count2}: PASS')
print('independent exhaustive vertex-level verification: PASS')
