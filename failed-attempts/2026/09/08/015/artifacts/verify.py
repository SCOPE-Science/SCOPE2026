#!/usr/bin/env python3
# verify.py v1.0 - one-command replay verifier (stdlib only, no SAT solver).
# Fast pure-Python checks + gcc rebuild/rerun of the archived C tools.
# Steps:
#  1. DIMACS headers/clause counts for F9/F8/F13.
#  2. Every model in models8.txt satisfies F8 (brute-force clause eval).
#  3. models8.txt: 17640 distinct entries; set-agrees with models8b.txt
#     (product of the INDEPENDENT second enumerator).
#  4. Rebuild + rerun enum8/enum8b from source; counts must be 17640 and the
#     model SETS must equal the archived files (completeness, twice over).
#  5. Extension UNSAT: rebuild + rerun ext9 (all 40,642,560 star completions
#     over all 17640 models x 9 deletion sites blocked) => F9 UNSAT given
#     completeness from step 4.
#  6. K13 witness: BITS satisfies F13 clauses + standalone triple/quintuple
#     enumeration (0 red triangles, 0 blue K5s); rebuild + rerun check13.
#  7. Isomorphism census: rebuild + rerun canon8 (OpenMP) and require byte-
#     identical classes8.txt (3 classes); pure-Python orbit-stabilizer +
#     rep-canonicality recheck on the 3 representatives only.
# Usage: python3 verify.py   (needs gcc; uses OpenMP if available)
import itertools, os, subprocess, sys
from math import comb

ART = os.path.dirname(os.path.abspath(__file__))
def P(f): return os.path.join(ART, f)
fails = []
def check(name, cond, info=""):
    print(("PASS " if cond else "FAIL ") + name + (" " + str(info) if info else ""), flush=True)
    if not cond: fails.append(name)

def run(cmd):
    r = subprocess.run(cmd, cwd=ART, capture_output=True, text=True, timeout=1200)
    return r

def load_dimacs(p):
    cls = []; nv = 0
    for ln in open(p):
        if ln.startswith("c"): continue
        if ln.startswith("p"): nv = int(ln.split()[2]); continue
        cls.append(list(map(int, ln.split()))[:-1])
    return nv, cls

# 1. DIMACS
for f, n, s, t in [("F9_34.cnf",9,3,4),("F8_34.cnf",8,3,4),("F13_35.cnf",13,3,5)]:
    nv, cls = load_dimacs(P(f))
    check("dimacs_"+f, nv == comb(n,2) and len(cls) == comb(n,s)+comb(n,t),
          "nv=%d ncl=%d" % (nv, len(cls)))

# 2. all models satisfy F8
nv8, cls8 = load_dimacs(P("F8_34.cnf"))
models = [l.strip() for l in open(P("models8.txt")) if l.strip()]
masks = [int(x, 16) for x in models]
def sat8(mask):
    a = [False]*29
    for e in range(28): a[e+1] = bool((mask >> e) & 1)
    return all(any((l > 0 and a[l]) or (l < 0 and not a[-l]) for l in c) for c in cls8)
bad = sum(1 for m in masks if not sat8(m))
check("models8_all_satisfy_F8", bad == 0 and len(masks) == 17640,
      "n=%d bad=%d" % (len(masks), bad))
check("models8_distinct", len(set(masks)) == 17640, "")

# 3. second enumerator set agreement
b = [l.strip() for l in open(P("models8b.txt")) if l.strip()]
check("two_enumerators_agree", set(b) == set(models) and len(b) == 17640, "b=%d" % len(b))

# 4. rebuild + rerun both enumerators
r = run(["gcc","-O2","-o","work_enum8","enum8.c"])
check("build_enum8", r.returncode == 0, r.stderr[-500:] if r.returncode else "")
r = run(["gcc","-O2","-o","work_enum8b","enum8b.c"])
check("build_enum8b", r.returncode == 0, r.stderr[-500:] if r.returncode else "")
if all(os.path.exists(P(x)) for x in ("work_enum8","work_enum8b")):
    r1 = run(["./work_enum8","8"])
    r2 = run(["./work_enum8b"])
    got1 = sorted(l.strip() for l in r1.stdout.split() if l.strip())
    got2 = sorted(l.strip() for l in r2.stdout.split() if l.strip())
    check("rerun_enum8_count", len(got1) == 17640, "n=%d %s" % (len(got1), r1.stderr.strip()))
    check("rerun_enum8b_count", len(got2) == 17640, "n=%d %s" % (len(got2), r2.stderr.strip()))
    check("rerun_enum8_set_matches_archive", got1 == sorted(models), "")
    check("rerun_enum8b_set_matches_archive", got2 == sorted(models), "")
    for x in ("work_enum8","work_enum8b"):
        try: os.remove(P(x))
        except OSError: pass

# 5. extension UNSAT (F9) via rebuilt ext9
r = run(["gcc","-O2","-o","work_ext9","ext9.c"])
check("build_ext9", r.returncode == 0, r.stderr[-500:] if r.returncode else "")
if os.path.exists(P("work_ext9")):
    r = run(["./work_ext9","models8.txt"])
    ok = r.returncode == 0 and "all_blocked=1" in r.stdout
    check("extension_UNSAT_F9", ok, (r.stdout+r.stderr).strip()[-200:])
    try: os.remove(P("work_ext9"))
    except OSError: pass

# 6. K13 witness
wit = [l for l in open(P("witness13.txt")) if l.startswith("BITS")]
bits = wit[0].split()[1].strip() if wit else ""
check("witness_bits_len", len(bits) == 78, len(bits))
if len(bits) == 78:
    n13, cls13 = load_dimacs(P("F13_35.cnf"))
    a = [False]*79
    for e,ch in enumerate(bits): a[e+1] = (ch == '1')
    nbad = sum(1 for c in cls13 if not any((l>0 and a[l]) or (l<0 and not a[-l]) for l in c))
    check("witness_satisfies_F13", nbad == 0, "violated=%d" % nbad)
    E13 = [(i,j) for i in range(13) for j in range(i+1,13)]
    R = [[0]*13 for _ in range(13)]
    for e,(u,v) in enumerate(E13): R[u][v] = R[v][u] = (1 if bits[e]=='1' else 0)
    nt = sum(1 for x,y,z in itertools.combinations(range(13),3) if R[x][y] and R[x][z] and R[y][z])
    nk = sum(1 for q in itertools.combinations(range(13),5)
             if all(R[q[i]][q[j]]==0 for i in range(5) for j in range(i+1,5)))
    check("witness_bruteforce", nt == 0 and nk == 0, "redtri=%d blueK5=%d/1287" % (nt, nk))
r = run(["gcc","-O2","-o","work_check13","check13.c"])
if r.returncode == 0 and len(bits) == 78:
    r = run(["./work_check13", bits])
    check("check13_rerun", r.returncode == 0 and "WITNESS_OK" in r.stdout, r.stdout.strip().splitlines()[-1] if r.stdout else "")
    try: os.remove(P("work_check13"))
    except OSError: pass

# 7. census: rebuild + rerun canon8, byte-compare; Python recheck of 3 reps
r = run(["gcc","-fopenmp","-O2","-o","work_canon8","canon8.c"])
if r.returncode != 0:  # fall back without OpenMP
    r = run(["gcc","-O2","-o","work_canon8","canon8.c"])
check("build_canon8", r.returncode == 0, r.stderr[-500:] if r.returncode else "")
if os.path.exists(P("work_canon8")):
    with open(P("models8.txt")) as f:
        r = subprocess.run(["./work_canon8"], cwd=ART, stdin=f, capture_output=True,
                           text=True, timeout=1200)
    arch = open(P("classes8.txt")).read()
    check("canon8_rerun_matches_archive", r.stdout == arch,
          "stderr=" + r.stderr.strip() + " classes=%d" % len(r.stdout.splitlines()))
    try: os.remove(P("work_canon8"))
    except OSError: pass

E8 = [(i,j) for i in range(8) for j in range(i+1,8)]
perms = list(itertools.permutations(range(8)))
def remap(mask, p):
    Rm = 0
    # bit k of mask = edge E8[k]; permute endpoints
    red = [[False]*8 for _ in range(8)]
    for k,(i,j) in enumerate(E8):
        if (mask >> k) & 1: red[i][j] = red[j][i] = True
    v = 0
    for k,(i,j) in enumerate(E8):
        u,w = p[i],p[j]
        if u > w: u,w = w,u
        if red[u][w]: v |= (1 << k)
    return v
reps = []
for ln in open(P("classes8.txt")):
    f = ln.split(); reps.append((int(f[0],16), int(f[1]), int(f[2]), f[3]))
check("nclasses", len(reps) == 3, len(reps))
ok = True; tot = 0
for (rc, cnt, aut, dg) in reps:
    tot += cnt
    if cnt*aut != 40320: ok = False; print("   orbit-stabilizer fail", hex(rc))
    if min(remap(rc, p) for p in perms) != rc: ok = False; print("   rep not canonical", hex(rc))
    au = sum(1 for p in perms if remap(rc, p) == rc)
    if au != aut: ok = False; print("   aut mismatch", hex(rc), au, aut)
    Rm = [[0]*8 for _ in range(8)]
    for k,(i,j) in enumerate(E8):
        if (rc >> k) & 1: Rm[i][j] = Rm[j][i] = 1
    if "".join(map(str, sorted(sum(Rm[i][j] for j in range(8)) for i in range(8)))) != dg:
        ok = False; print("   degseq mismatch", hex(rc))
check("reps_orbit_stabilizer_canon", ok and tot == 17640, "tot=%d" % tot)
canons = [min(remap(rc, p) for p in perms) for rc,_,_,_ in reps]
check("reps_pairwise_noniso", len(set(canons)) == 3, "")

print("RESULT " + ("ALL_OK" if not fails else "FAILURES=%s" % fails))
sys.exit(1 if fails else 0)
