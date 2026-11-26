# Independent mathematical audit

## correctness

PASS

Reduction by nb=(n+1)a and nc=(n+1)b gives a nonnegative normal form; reducing first modulo n and then dividing after removal of jc determines the two bounded digits. For residue un+j, its quotient threshold is u−j+(n+1)ceil((2j−u)/n). Within a row of residues it decreases by one except for jumps of size n at j=floor(u/2)+1 and, precisely when u≤n−3, j=floor((n+u)/2)+1. At the boundary from u to u+1 the preceding threshold is at least u+2 and the next is u+1; multiples of a cannot start a gap block. Each positive jump supplies exactly n consecutive lifts giving the two disjoint progression families. The maximum and sum of the rectangle give the stated Frobenius number and genus. The coefficient of (1−z) times the membership generating function is a successive indicator difference, so each maximal gap block contributes exactly two changes, plus the constant coefficient counted separately. For n=2 there are four starts 1,5,7,11 and support nine. The separately authored reachability check /workspace/branches/2f35973e-7263-48b0-be6d-395a6258d6ef/independent_gap_check.py matched starts, genus, conductor and support for n=2..40; log independent_gap_check_chunks.txt. The frozen checker was inspected, not executed. The residue argument, not the finite test, proves the quantifiers.

## originality

PASS

Pass is for the explicit progressions of ordinary maximal-gap starts and their exact sparsity consequence. The geometric family, Apéry rectangle, Frobenius number, genus and general Hilbert-series formula are prior results. The strongest publications include this very family and encode its gap set, but the inspected formulas do not supply the specialization's adjacent-residue jump analysis or a stronger spacing result from which its output follows immediately.

## value

PASS

This is a natural short geometric semigroup family. The progression description identifies all negative coefficients and counts all maximal holes without expanding a cubic-degree polynomial. It gives an exact adjacency invariant with quadratic support rather than duplicating the known genus or Frobenius number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
