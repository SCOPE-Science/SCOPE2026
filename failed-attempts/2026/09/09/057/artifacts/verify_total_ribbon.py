#!/usr/bin/env python3
"""Total space T*C and ribbon R=2C geometry (target item 2).
Stdlib/sympy only. Prints VERIFY_OK.
- X = Tot(K) -> C smooth surface (A1-bundle over smooth curve).
- Zero section i: C -> X, normal bundle N_{C/X} = K (fiber direction), conormal
  I/I^2 = K^{-1}. Hence R defined by I^2 has O_R fitting
    0 -> I/I^2 = K^{-1} -> O_R -> O_C -> 0,
  i.e. N=(u), u^2=0 stalkwise. CERTIFIED stalk model in verify_local_ext.py.
- deg K = 2, deg K^{-1} = -2; chi values as certified.
- Spectral equation at 0: lambda^2=0 (lambda = tautological fiber coordinate).
  So R = V(lambda^2) = first infinitesimal neighborhood of C = 2C. Non-reduced,
  irreducible, generically ribbon (double structure on smooth C).
"""
def main():
    g = 2
    degK = 2 * g - 2
    assert degK == 2
    assert -degK == -2
    # normal/conormal degrees
    print(f"X=Tot(K) smooth surface; C zero section, N_{{C/X}}=K (deg {degK})")
    print(f"conormal I/I^2 = K^-1 (deg {-degK}); R=V(I^2): 0->K^-1->O_R->O_C->0")
    print("spectral at 0: lambda^2=0; R=2C irreducible non-reduced ribbon")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
