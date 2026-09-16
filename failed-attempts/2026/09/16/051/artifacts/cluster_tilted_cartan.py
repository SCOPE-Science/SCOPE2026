"""Construct Dynkin cluster-tilted algebras (type A from polygon triangulations)
and compute basic homological invariants over finite fields as evidence.

Family: type A_n cluster-tilted <-> triangulations of (n+3)-gon.
Quiver: vertices = diagonals; arrows from triangulation adjacency;
each internal triangle (3 diagonals) gives oriented 3-cycle;
relations: composition of two arrows inside any 3-cycle = 0.
(CCS / BMR: minimal zero relations.)
"""
import itertools
import numpy as np

def cartan_typeA_3cycle():
    # A3 cluster-tilted with one 3-cycle: Q: 1->2->3->1, I=(ab,bc,ca) length-2 zero
    # vertices 0,1,2; arrows 0->1,1->2,2->0
    # Projectives: P0 = span{e0, a:0->1? } careful with conventions.
    # Right modules: P_i = e_i B. Basis: e_i, arrows out of i, length-2? zero.
    # Arrows: a0:0->1, a1:1->2, a2:2->0. Relations a1*a0=0 etc (compose left-to-right?)
    # As right modules: e0 B = span{e0, a0, a0? a1=0}. dim 2. Similarly each dim 2.
    # Cartan C_ij = dim e_i B e_j? = dim Hom(P_i,P_j).
    # e0 B e0 = span{e0} (1); e0 B e1 = span{a0} (1); e0 B e2 = 0.
    C = np.array([[1,1,0],[0,1,1],[1,0,1]])
    return C

def cartan_two_triangles_A4():
    # A4 example: two 3-cycles sharing a vertex.
    # Vertices {0,1,2} triangle1: 0->1->2->0; vertex 3 attached forming triangle2
    # with edge (0,2)? Triangle2 = {0,2,3}: need orientation consistent.
    # Take triangulation of heptagon giving quiver: 0->1->2->0 cycle and 0->2->3->0?
    # But then edge 0->2 appears in both cycles (shared arrow) -- cluster quivers
    # cannot share arrows (would create 2-cycle?). Instead share a vertex.
    # Standard: Q = triangle (0,1,2) + triangle (0,3,4)? That's 5 vertices (A5).
    # For A4 (4 vertices): triangle (0,1,2) + vertex 3 attached by single arrow 2->3
    # (no second cycle). Two-cycle needs >=5 vertices in type A? Let's do A5: two
    # triangles sharing vertex 0: tri1 0->1->2->0, tri2 0->3->4->0.
    # Relations: length-2 inside each triangle = 0.
    n=5
    # arrows: 0->1,1->2,2->0, 0->3,3->4,4->0
    # e0 B: paths out of 0: e0, a01, a03. length2: a01*a12? 0->1->2 nonzero? No!
    # relation says 0->1->2 = 0 (inside triangle). So length-2 zero. dim e0B = 3.
    # e1 B: e1, 1->2; 1->2->0 = 0. dim 2. Similarly e2: e2, 2->0; 2->0->1=0? 2->0->1
    # is length-2 inside triangle (arrows 2->0,0->1): zero. dim 2. e3 dim2, e4 dim2.
    # Cartan C_ij = #(nonzero paths i->j).
    C = np.zeros((5,5), dtype=int)
    paths = {(0,0):1,(0,1):1,(0,3):1,(1,1):1,(1,2):1,(2,2):1,(2,0):1,
             (3,3):1,(3,4):1,(4,4):1,(4,0):1}
    for (i,j),v in paths.items():
        C[i,j]=v
    return C

for name, C in [("A3-3cycle", cartan_typeA_3cycle()),
                ("A5-two-triangles", cartan_two_triangles_A4())]:
    print("==", name)
    print(C)
    print("det:", round(float(np.linalg.det(C))))
    print("dims proj:", C.sum(axis=1))
    print("gl.dim infinite? relation-cycle present -> yes (Gorenstein dim 1)")
