"""Standalone exact finite checks for a modular scattered-pair syntactic monoid.

Run: python3 check_rees.py

The theorem for all moduli is proved mathematically; these computations are
independent finite cross-checks, not a replacement for that proof.
"""
from collections import deque
from itertools import product


def signature(word, m):
    if not word:
        return ('identity',)
    if '11' in word:
        return ('zero',)
    z = p = o = 0
    for c in word:
        if c == '0':
            z += 1
        else:
            o += 1
            p += z
    return (int(word[0]), z % m, o % m, p % m, int(word[-1]))


def multiply(a, b, m):
    if a == ('zero',) or b == ('zero',):
        return ('zero',)
    if a == ('identity',):
        return b
    if b == ('identity',):
        return a
    f, z, o, p, l = a
    ff, zz, oo, pp, ll = b
    if l == ff == 1:
        return ('zero',)
    return (f, (z + zz) % m, (o + oo) % m,
            (p + pp + z * oo) % m, ll)


def transitions(m):
    states = [(z, p, l) for z in range(m)
              for p in range(m) for l in (0, 1)] + [None]
    ids = {s: i for i, s in enumerate(states)}
    tables = []
    for c in '01':
        result = []
        for s in states:
            if s is None:
                ns = None
            else:
                z, p, l = s
                if c == '0':
                    ns = ((z + 1) % m, p, 0)
                elif l:
                    ns = None
                else:
                    ns = (z, (p + z) % m, 1)
            result.append(ids[ns])
        tables.append(tuple(result))
    return states, tables


def run():
    for m in range(2, 8):
        states, tables = transitions(m)
        size = len(states)
        identity = tuple(range(size))
        sig2trans = {('identity',): identity}
        trans2sig = {identity: ('identity',)}
        queue = deque([identity])
        seen_words = {identity: ''}
        while queue:
            trans = queue.popleft()
            word = seen_words[trans]
            for letter, t in zip('01', tables):
                new_trans = tuple(t[q] for q in trans)
                new_word = word + letter
                sig = signature(new_word, m)
                # Each signature is precisely one transition action.
                previous = sig2trans.setdefault(sig, new_trans)
                assert previous == new_trans, ('signature mismatch', m, new_word)
                prior_sig = trans2sig.setdefault(new_trans, sig)
                assert prior_sig == sig, ('nonfaithful signature', m, new_word)
                assert multiply(signature(word, m), signature(letter, m), m) == sig
                if new_trans not in seen_words:
                    seen_words[new_trans] = new_word
                    queue.append(new_trans)
        target = 4 * m**3 + 2
        assert len(seen_words) == len(sig2trans) == len(trans2sig) == target
        # Independently compare direct subsequence counting and DFA acceptance.
        for n in range(0, 13):
            for letters in product('01', repeat=n):
                w = ''.join(letters)
                x = 0
                for letter in w:
                    x = tables[int(letter)][x]
                expected = ('11' not in w and sum(
                    w[i] == '0' and w[j] == '1'
                    for i in range(len(w)) for j in range(i+1, len(w))) % m == 0)
                actual = states[x] is not None and states[x][1] == 0
                assert actual == expected, (m, w)
                assert signature(w, m) in sig2trans
        print(f'm={m}: {target} transition maps = {target} normal forms; '
              f'{size} DFA states; lengths 0..12 checked')
    print('PASS: all independent finite checks')

if __name__ == '__main__':
    run()
