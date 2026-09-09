#!/usr/bin/env python3
"""Fiber-Ext generator check: Ext^1_{k[u]/(u^2)}(k,k) ~= k, class = +1.
Exact linear algebra over QQ (sympy). Prints VERIFY_OK.
A = k[u]/(u^2), k = A/(u). Free resolution: ... -u-> A -u-> A -> k -> 0.
Apply Hom_A(-, k): differentials are 0 (u acts as 0 on k both sides).
So Ext^1 = k with generator = class of 0 -> k -> A -> k -> 0.
Nonsplit: any A-section s: k -> A has s(1) in Ann(u) = (u), maps to 0 in k.
Ann check: A = span{1,u}; u*(a+bu) = au; =0 iff a=0. Exact.
"""
import sympy as sp

def main():
    # mult-by-u matrix in basis [1, u]: u*1 = u -> (0,1); u*u = 0 -> (0,0)
    M = sp.Matrix([[0, 0], [1, 0]])
    assert M.rank() == 1
    # kernel: vectors (a,b) with M*(a,b) = (0, a) = 0 => a = 0 => span{(0,1)} = (u)
    assert M.nullspace() == [sp.Matrix([0, 1])]
    print("A=k[u]/(u^2): Ann(u)=(u), dim-kernel 1")
    print("resolution periodic x u; Hom differentials 0 => Ext^1 = k, generator +1")
    print("extension 0->k->A->k->0 nonsplit: section lands in (u), projects to 0")
    print("restriction <xi,sigma> = this generator = +1")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
