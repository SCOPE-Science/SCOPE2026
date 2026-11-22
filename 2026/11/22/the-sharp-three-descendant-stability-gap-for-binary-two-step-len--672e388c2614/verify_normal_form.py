"""Independent RC2 run-form enumeration of all boundary-defect descendants."""
from collections import Counter

def rc2(w, i):
    t = w[i:i+2]
    insert = ''.join('0' if b == '1' else '1' for b in t[::-1])
    return w[:i+2]+insert+w[i+2:]

def descendants(w):
    return {rc2(rc2(w,i),j)
            for i in range(len(w)-1) for j in range(len(w)+1)}

def classified(n):
    result = set()
    # Three zeros: the unique alternating prefix and the single double-zero run.
    result.add('01010'+'1'*(n-1))
    for a in range(2,n):
        result.add('0'+'1'*a+'00'+'1'*(n+1-a))
    # Four zeros: singleton then pair, or pair then singleton.
    for b in range(2,n):
        result.add('010'+'1'*b+'00'+'1'*(n-1-b))
    for a in range(2,n):
        result.add('0'+'1'*a+'0100'+'1'*(n-a-1))
    for a in range(2,n-1):
        result.add('0'+'1'*a+'0010'+'1'*(n-a-1))
    # Five zeros: two zero pairs after the original leading zero.
    for a in range(2,n):
        for b in range(n-a):
            c = n-1-a-b
            result.add('0'+'1'*a+'00'+'1'*b+'00'+'1'*c)
    return result

def run():
    for n in range(4, 61):
        direct = descendants('0'+'1'*(n-1))
        forms = classified(n)
        assert direct == forms, (n, len(direct), len(forms), sorted(direct^forms)[:5])
        freq = Counter(s.count('0') for s in direct)
        assert freq == {3:n-1, 4:3*n-7, 5:(n-1)*(n-2)//2}
        assert len(direct) == (n*n+5*n-14)//2
        if n in (4,5,8,16,32,60):
            print(f'n={n}: {freq}, total={len(direct)}')

if __name__ == '__main__':
    run()

def classified_right(n):
    forms = set()
    for a in range(2,n):
        forms.add('1'*a+'00'+'1'*(n+1-a)+'0')
    forms.add('1'*(n-1)+'00011')
    forms.add('1'*(n-1)+'01010')
    for a in range(2,n-1):
        forms.add('1'*a+'0010'+'1'*(n-a-1)+'0')
    for a in range(2,n):
        forms.add('1'*a+'00'+'1'*(n-a-1)+'010')
        forms.add('1'*a+'0100'+'1'*(n-a-1)+'0')
    for a in range(2,n):
        for b in range(n-a):
            c = n-1-a-b
            forms.add('1'*a+'00'+'1'*b+'00'+'1'*c+'0')
    return forms

def check_right():
    for n in range(4,61):
        actual = descendants('1'*(n-1)+'0')
        forms = classified_right(n)
        assert actual == forms, (n, actual ^ forms)
        freq = Counter(s.count('0') for s in actual)
        assert freq == {3:n, 4:3*n-8, 5:(n-1)*(n-2)//2}
    print('Right-boundary RC2 normal form verified through length 60.')

if __name__ == '__main__':
    check_right()
