"""Direct transitions, structural invariants, and independent LCS recurrence."""


def explicit(n):
    if n == 2: return 'ab'
    if n == 3: return 'abbaab'
    if n == 4: return 'abbaaabaaabbba'
    return ('abb'+('a'*(n-1)+'b')*(n-3)+'aa'
            +('b'*(n-1)+'a')*(n-5)+'b'*(n-1)+'aa'+'b'*(n-1)+'a')


def apply(initial, n, word, swap):
    current = list(initial)
    for char in word:
        is_rotation = (char == 'a') != swap
        next_states = []
        for pos in current:
            next_states.append((pos+1)%n if is_rotation else (0 if pos==n-1 else pos))
        current = sorted(set(next_states))
    return current


def lcs(p, q):
    prev = [0] * (len(q)+1)
    for letter in p:
        curr = [0]*(len(q)+1)
        for j, v in enumerate(q, start=1):
            curr[j] = prev[j-1]+1 if letter == v else max(curr[j-1], prev[j])
        prev = curr
    return prev[-1]


def main():
    for n in range(2, 51):
        w = explicit(n)
        assert len(w) == 2*(n*n-3*n+3)
        assert len(apply(range(n), n, w, False)) == 1
        assert len(apply(range(n), n, w, True)) == 1
        if n >= 5:
            prefix = 'abb'+('a'*(n-1)+'b')*(n-3)
            assert apply(range(n),n,prefix,False) == [0,1]
            assert apply(range(n),n,prefix,True) == list(range(1,n-2))+[n-1]
            assert apply(range(n),n,prefix+'aa',False) == [2,3]
            assert apply(range(n),n,prefix+'aa',True) == list(range(n-2))
        if n <= 30:
            p = 'b'+('a'*(n-1)+'b')*(n-2)
            q = 'a'+('b'*(n-1)+'a')*(n-2)
            assert lcs(p,q) == 2*(n-2)
    print('VERIFY_STRUCTURE_OK: exact images and witness lengths n=2..50;')
    print('LCS checked independently for n=2..30; intermediate invariants n=5..50')


if __name__ == '__main__':
    main()
