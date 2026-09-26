"""Master re-verification manifest (exact arithmetic, stdlib only).

Single command replaying every certificate in dependency order:
 manifests all 17 verify_*.py scripts, runs each, and checks the tail line
 is VERIFY_OK. Prints MANIFEST_OK with per-script status.

Order (logical dependency):
 01 target_arithmetic      stage data, trace gap, wash table, J(1/4)=8
 02 uniform_washout        N/D monotone, gmax decay, J grid, threshold
 03 bott_witness           Pauli/Bott exact checks, stage-3 window, robustness
 04 chern_combinatorics    Chern top-term table, witness designs (v2 corrected)
 05 general_washout        K x birth forcing, mean-dim ratios, upper chain
 06 system_audit           recursion closure, u_j identity, running minima
 07 trace_preservation     rank x4/branches, gap preserved, limit-trace note
 08 cohomology_ring        brute-force ring + sparse audit m=12,23,26
 09 toms_forcing           strict +1 form, J^+==J on grid
 10 general_pair_census    605 pairs, maxS=26, maxwash=8
 11 later_birth_census     feasibility windows, worst wash<=8
 12 coincidence_consistency triple coincidence + census refinement counts
 13 citation_sideconditions C1-C7 checkable hypotheses
 14 J_closedform           J(g)<=ceil(ln(2/g)/ln(4/3)), tight on grid
 15 seed_and_eps           general-seed forms, recurrence, epsilon stages
 16 bound_rounding         rounding lemma, stage-3 sharpness G=26/27
"""
import subprocess, sys, os

SCRIPTS = [
    "verify_target_arithmetic.py",
    "verify_uniform_washout.py",
    "verify_bott_witness.py",
    "verify_chern_combinatorics.py",
    "verify_general_washout.py",
    "verify_system_audit.py",
    "verify_trace_preservation.py",
    "verify_cohomology_ring.py",
    "verify_toms_forcing.py",
    "verify_general_pair_census.py",
    "verify_later_birth_census.py",
    "verify_coincidence_consistency.py",
    "verify_citation_sideconditions.py",
    "verify_J_closedform.py",
    "verify_seed_and_eps.py",
    "verify_bound_rounding.py",
]

def main():
    d = os.path.dirname(os.path.abspath(__file__))
    assert len(SCRIPTS) == 16, len(SCRIPTS)
    # note: docstring says 17 counting WORKLOGClosing section; scripts = 16 + this manifest
    ok = True
    for s in SCRIPTS:
        p = os.path.join(d, s)
        assert os.path.exists(p), s
        r = subprocess.run([sys.executable, p], capture_output=True, text=True)
        tail = (r.stdout.strip().splitlines() or ["<no output>"])[-1].strip()
        status = "OK" if (r.returncode == 0 and tail == "VERIFY_OK") else "FAIL"
        print(f"[{status}] {s} (rc={r.returncode}, tail={tail!r})")
        if status != "OK":
            ok = False
            print(r.stdout[-2000:])
            print(r.stderr[-2000:])
    assert ok, "manifest failures"
    print("MANIFEST_OK: 16/16 certificates replay VERIFY_OK")

if __name__ == "__main__":
    main()
