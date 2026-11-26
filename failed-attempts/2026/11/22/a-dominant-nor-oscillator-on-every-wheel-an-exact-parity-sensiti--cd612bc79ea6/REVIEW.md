# Independent mathematical audit

## correctness

PASS

On active vertex sets define F(S)=V\N(S). By symmetry S⊆F²(S), so applying the antitone F gives F³(S)⊆F(S); the inclusion applied to F(S) gives the reverse. Thus the selected basin is exactly the union of the two one-step inverse fibers. With no isolated vertices these are {empty} (inverse of full) and the total dominating sets (inverse of empty). On K₁∨Cₙ, among the latter those containing the hub can have any nonempty rim subset; those omitting it are precisely the total dominating sets of Cₙ. The latter forbid two zeros at separation two, so the transfer-trace computation gives the Lucas value on each step-two component. For n=4 those components are edges rather than simple length-two cycles, and the cyclic word trace still correctly counts three patterns for each edge. A hub-on, nonempty nonfull rim state reaches empty but is not on its orbit, proving sharpness. Exact tuple-state orbit replay /workspace/replays/2.py covers both graph families at n=3..12; wheel/bare counts are 12/5 at n=3, 25/10 at n=4, and 4420/325 at n=12, with worst transient one. Binet's formula and Bₙ>2ⁿ justify the stated probability asymptotic and dominance.

## originality

FAIL

The exact wheel-basin law is already covered in equivalent form by the total-domination-polynomial result for joins together with the enumerated cycle case. The conversion from total domination to the specified NOR basin is an immediate identity for all undirected graphs with no isolated vertices; it is not a new wheel-specific classification. The already known odd-ring NOR result gives the odd comparison directly. No assertion is made that the exact wheel-basin wording occurs in the prior literature.

## value

FAIL

The comparison of basin probabilities is a useful illustration, but the proposed invariant is a direct translation of a known join enumeration; the one-step identity holds on every undirected graph and the sharpness example and parity corrections are elementary consequences. As frozen there is no further nonmechanically implied wheel invariant or classification to justify an independent finding. The exhaustive replay is useful for correctness, not new scientific content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
