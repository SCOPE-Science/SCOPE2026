"""Independent replay: reruns every step and asserts all key identities."""
import subprocess, sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = ["s1_gleason.py", "s2b_shorten.py", "s3b_shadow_exact.py", "s4_theta.py",
         "s5_double.py", "s6b_codetheta.py", "s6c_normalization.py", "s7_design.py",
         "s8_moments.py", "s9_double_system.py", "s10_triple_system.py",
         "s16_kpt_system.py", "s17_tables.py", "s18_jacobi.py",
         "s19_kscreens.py", "s27_derived.py", "s28_involution.py",
         "f1_gap.py", "f2_table.py"]
EXTRA_ARGS = {"s16_kpt_system.py": ["4"]}
for s in STEPS:
    args = [sys.executable, os.path.join(HERE, s)] + EXTRA_ARGS.get(s, [])
    r = subprocess.run(args, capture_output=True, text=True)
    print("=" * 12, s, "rc=", r.returncode)
    print((r.stdout or "")[-300:])
    if r.returncode != 0:
        print(r.stderr[-2000:])
        sys.exit(1)
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
assert A[0] == 1 and A[4] == 0 and A[8] == 0 and A[12] == 0
assert A[16] == 249849 and A[36] == 25756721120 and A[72] == 1
assert sum(A) == 2 ** 36
sh = json.load(open(os.path.join(HERE, "shadow_exact.json")))
assert all(sh[str(v)][2] for v in range(73) if sh[str(v)][0] or sh[str(v)][1])
assert all((sh[str(v)][0] or 0) == A[v] for v in range(73)), "self-shadow"
ss = json.load(open(os.path.join(HERE, "shorten_system.json")))
assert ss["consistent"] and ss["free"] == []
th = json.load(open(os.path.join(HERE, "theta_trace.json")))["theta"]
assert th[4] == 6218175600
d9 = json.load(open(os.path.join(HERE, "s9_double_system.json")))
assert d9["consistent"] and d9["equals_balanced"]
d10 = json.load(open(os.path.join(HERE, "s10_triple_system.json")))
assert d10["consistent"] and d10["equals_balanced"]
dg = json.load(open(os.path.join(HERE, "s7_design.json")))
assert dg["am_violations"] == []
ft = json.load(open(os.path.join(HERE, "fallback_table.json")))
assert ft["n MacWilliams-compatible distributions"] == 1
assert ft["min_distance"] == 16 and ft["dual_distance"] == 15
assert ft["gap_g"] == 34359738368 == 2 ** 35
assert sum(ft["Aprime"]) == 2 ** 35 and sum(ft["Bprime"]) == 2 ** 36
fg = json.load(open(os.path.join(HERE, "fallback_gap.json")))
assert fg["g"] == 34359738368 and fg["Q_total"] == 2 ** 35
print("VERIFY_OK")
