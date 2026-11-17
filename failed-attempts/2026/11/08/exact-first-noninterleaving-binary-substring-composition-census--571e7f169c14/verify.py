"""Independent reproducibility checks for binary substring-composition classes."""
import collections
import itertools
import pathlib
import subprocess
import tempfile
import sys

ROOT = pathlib.Path(__file__).resolve().parent
N = 23
EXPECTED = {1: 4096, 2: 4191936, 4: 160}

def word(x):
    return ''.join(str((x >> i) & 1) for i in range(N))

def parikh_profile(s):
    pref = [0]
    for b in s: pref.append(pref[-1] + (b == '1'))
    return tuple(tuple(sum(pref[i + k] - pref[i] == t for i in range(N - k + 1))
                       for t in range(k + 1)) for k in range(1, N + 1))

def factors(s):
    result = []
    for d in range(2, N + 1):
        if (N + 1) % d: continue
        a = d - 1
        b = (N + 1)//d - 1
        if b == 0: continue
        core = s[:a]
        if all(s[j*d:j*d+a] == core for j in range(b + 1)):
            outer = ''.join(s[j*d+a] for j in range(b))
            result.append((core, outer))
    return result

def variants(s):
    yield s[::-1]
    for a,b in factors(s):
        def join(x,y): return ''.join(x+c for c in y)+x
        yield join(a[::-1],b)
        yield join(a,b[::-1])

def closure(s):
    seen={s}; todo=[s]
    for z in todo:
        for t in variants(z):
            if t not in seen:
                seen.add(t)
                todo.append(t)
    return seen

def groups_from_text(text):
    groups=[]
    for line in text.splitlines():
        vals = [int(v) for v in line.split()]
        if len(vals) == 5 and vals[0] == 4:
            group=tuple(sorted(vals[1:]))
        elif len(vals) == 4:
            group=tuple(sorted(vals))
        else:
            raise AssertionError(f'invalid group line: {line}')
        groups.append(group)
    assert len(groups) == len(set(groups)) == 160
    return sorted(groups)

def verify_groups(groups):
    allmembers=set()
    exceptions=[]
    generated=0
    for g in groups:
        assert len(set(g)) == 4
        allmembers.update(g)
        ws=[word(x) for x in g]
        signatures=[parikh_profile(s) for s in ws]
        assert all(key == signatures[0] for key in signatures)
        factors_present=[bool(factors(s)) for s in ws]
        assert len(set(factors_present)) == 1
        if factors_present[0]:
            assert closure(ws[0]) == set(ws)
            generated += 1
        else:
            assert closure(ws[0]) == set(ws[0:1] + [ws[0][::-1]])
            exceptions.append(g)
    assert len(allmembers) == 640
    assert generated == 152 and len(exceptions) == 8
    masks=(1 << N)-1
    missing=[]
    for group in exceptions:
        gset=set(group)
        complement=frozenset(masks ^ x for x in group)
        assert any(complement == frozenset(other) for other in exceptions)
    exception_orbits={min(tuple(g),tuple(sorted(masks ^ x for x in g))) for g in exceptions}
    assert len(exception_orbits) == 4
    print('COMPOSITION_AND_INTERLEAVING_OK groups=160 interleaved=152 exceptional=8 complement_orbits=4')
    return exceptions

def full_replay():
    with tempfile.TemporaryDirectory() as d:
        tmp = pathlib.Path(d)
        answers=[]
        for src,exe in [('exact_census.cpp','exact'),('independent_census.cpp','independent')]:
            subprocess.run(['g++','-std=c++17','-O3',str(ROOT/src),'-o',str(tmp/exe)],check=True)
            run = subprocess.run([str(tmp/exe),'23'],cwd=tmp,capture_output=True,text=True,check=True,timeout=180)
            print(run.stdout.strip())
            if src == 'exact_census.cpp':
                assert 'profiles=4196192 heavy=160 hash_collision_groups=0' in run.stdout
                for k,v in EXPECTED.items():
                    assert f'size={k} classes={v}' in run.stdout
                answers.append(groups_from_text((tmp/'equicomposable_23.txt').read_text()))
            else:
                assert 'collisions=0' in run.stdout
                for k,v in EXPECTED.items():
                    assert f'class_size={k} class_count={v}' in run.stdout
                answers.append(groups_from_text((tmp/'independent_four_23.txt').read_text()))
        assert answers[0] == answers[1] == groups_from_text((ROOT/'FOUR_CLASSES.txt').read_text())
        print('TWO_INDEPENDENT_FULL_CENSUSES_OK n=23 words=8388608 profiles=4196192')

if __name__ == '__main__':
    groups = groups_from_text((ROOT/'FOUR_CLASSES.txt').read_text())
    exceptions=verify_groups(groups)
    for i,g in enumerate(exceptions,1):
        print('EXCEPTION_%d'%i,*[word(x) for x in g])
    if '--full' in sys.argv:
        full_replay()
    print('VERIFICATION_OK')
