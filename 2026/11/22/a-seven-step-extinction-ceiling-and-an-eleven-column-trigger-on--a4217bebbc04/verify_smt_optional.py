"""Independent SMT cross-check of the finite three-row Greenberg--Hastings certificate.

Run: python3 verify_smt_optional.py
Requires the ordinary libz3 shared library. The exact self-contained
ternary BDD verification is in verify_bdd.py.
"""
import ctypes
import ctypes.util

libname = ctypes.util.find_library('z3')
if not libname:
    raise SystemExit('libz3 unavailable: the independent SMT cross-check is optional')
lib = ctypes.CDLL(libname)
lib.Z3_mk_config.restype = ctypes.c_void_p
lib.Z3_mk_context.argtypes = [ctypes.c_void_p]
lib.Z3_mk_context.restype = ctypes.c_void_p
lib.Z3_eval_smtlib2_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.Z3_eval_smtlib2_string.restype = ctypes.c_char_p
lib.Z3_del_context.argtypes = [ctypes.c_void_p]
lib.Z3_del_config.argtypes = [ctypes.c_void_p]

def is_excitable(n, t):
    conf = lib.Z3_mk_config()
    ctx = lib.Z3_mk_context(conf)
    def name(kind, r, c, k):
        return f'{kind}{k}_{r}_{c}'
    statements = ['(set-option :timeout 20000)']
    for k in range(t+1):
        for c in range(n):
            for r in range(3):
                for kind in ('e', 'z'):
                    statements.append(f'(declare-fun {name(kind,r,c,k)} () Bool)')
                if k == 0:
                    statements.append(f'(assert (not (and {name("e",r,c,0)} {name("z",r,c,0)})))')
                    continue
                statements.append(f'(assert (= {name("z",r,c,k)} {name("e",r,c,k-1)}))')
                neighbors = [name('e',rr,cc,k-1) for rr,cc in
                             ((r-1,c),(r+1,c),(r,c-1),(r,c+1))
                             if 0 <= rr < 3 and 0 <= cc < n]
                pairs = [f'(and {neighbors[i]} {neighbors[j]})'
                         for i in range(len(neighbors)) for j in range(i+1,len(neighbors))]
                trigger = '(or ' + ' '.join(pairs) + ')' if pairs else 'false'
                expr = (f'(and (not {name("e",r,c,k-1)}) '
                        f'(not {name("z",r,c,k-1)}) {trigger})')
                statements.append(f'(assert (= {name("e",r,c,k)} {expr}))')
    target = ' '.join(name('e',r,c,t) for r in range(3) for c in range(n))
    statements.append(f'(assert (or {target}))')
    statements.append('(check-sat)')
    reply = lib.Z3_eval_smtlib2_string(ctx, '\n'.join(statements).encode()).decode().strip()
    lib.Z3_del_context(ctx)
    lib.Z3_del_config(conf)
    if reply not in ('sat', 'unsat'):
        raise RuntimeError(f'Inconclusive SMT response: {reply}')
    return reply == 'sat'

if __name__ == '__main__':
    for n in range(1,14):
        last = max(t for t in range(7) if is_excitable(n,t))
        assert (last + 2) == (3,3,4,4,5,5,6,6,6,6,7,7,7)[n-1]
        assert not is_excitable(n,6)
        print('independent SMT passed', n, last+2)
