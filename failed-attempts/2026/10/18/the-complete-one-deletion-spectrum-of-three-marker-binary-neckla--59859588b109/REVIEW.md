# Independent mathematical audit

## correctness

PASS

The rotation-only source quotient is exactly cyclic triples of zero gaps. The marker-deletion outputs are unordered complementary pairs {x,s−x}; distinct positive gaps can be complementary only if the third gap is zero. The two nonidentity cyclic shifts in the comparison of (a−1,b,c) with (a,b−1,c) yield exactly a=b=c or a=b=c+1, including (1,1,0). Thus all deletion collisions are exhausted, and the two weight classes of outputs are disjoint. Anchoring at the sole zero gap gives s−1 ordered positive pairs, the repeated positive value ranges from 1 to floor((s−1)/2), and inclusion–exclusion on equalities of positive ordered triples gives the stated numerator for C_{s,6}, divided by their orbit size three. Burnside gives the stated total, including the periodic equal-gap orbit. s=0 and s=2 give the claimed exceptions; (1,2,s−3) witnesses B=6 for every s≥6. The mean defect numerator is 4C_{s,2}+3C_{s,3}+2C_{s,4}+C_{s,5}=2s+f_s+2+3e_s+z_s+h_s; the number outside the size-six class is s+f_s. These and N_s=s²/6+O(s) verify both asymptotics. RESULT.md lines 51–77 prove the full family; the reviewed verify.py is finite corroboration, not used as proof. The wording about labeled-word sampling should be read as a distinction between sampling conventions, not as saying they differ at every length: if 3 does not divide s, the label multiplicities are all equal.

## originality

FAIL

Exact equivalent coverage exists in a distinct indexed record, not the assigned record returned under an alias. Its rotation-only three-one, exact-one-deletion shadow generating functions recover every histogram coefficient, its gap proof has the same pointwise exceptions, and the mean and sharper asymptotics are direct weighted sums and expansions of those counts. No noncovered scientific increment was found. This is a statement about independently verifiable overlap in the current corpus, not evidence that the November record preceded the October record, or a finding about historical authorship or priority.

## value

PASS

As a mathematical result this is a complete infinite-family degree census for a natural sparse cyclic deletion channel: it separates period-driven and genuine cross-position collisions, identifies the length-nine onset of the generic degree, and quantifies ambiguity under uniform sampling. This is more informative than simply enumerating input necklaces. Mathematical usefulness does not make it a distinct contribution given the exact equivalent record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
