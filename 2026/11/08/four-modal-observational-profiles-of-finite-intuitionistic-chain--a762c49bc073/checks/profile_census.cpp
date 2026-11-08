#include <algorithm>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

// Four intuitionistic modalities on the upset algebra of a finite chain.
// Each nonempty row is represented by its minimum and maximum target.
// Its multiplicity is the number of possible choices of interior targets.
struct RowType { int min_target, max_target; uint64_t multiplicity; };

int main() {
    for (int n = 1; n <= 5; ++n) {
        std::vector<RowType> row_types{{n, -1, 1}};
        for (int a = 0; a < n; ++a)
            for (int b = a; b < n; ++b)
                row_types.push_back({a, b, a == b ? 1ULL : (1ULL << (b - a - 1))});
        std::vector<int> a(n), b(n);
        std::unordered_map<uint64_t, uint64_t> fibre;
        uint64_t represented_relations = 0;

        // Each of 4*n fields lies in [0,n], so three bits suffice for n<=5.
        // The resulting key occupies at most 60 bits, with no truncation.
        auto key = [&]() -> uint64_t {
            uint64_t code = 0;
            auto push = [&](int x) { code = (code << 3) | uint64_t(x); };
            int current = -1;
            for (int i = 0; i < n; ++i) { current = std::max(current, b[i]); push(current + 1); }
            std::vector<int> suffix_b(n), suffix_a(n);
            current = n;
            for (int i = n-1; i >= 0; --i) { current = std::min(current, b[i]); suffix_b[i] = current; }
            for (int i = 0; i < n; ++i) push(suffix_b[i] + 1);
            current = -1;
            for (int i = 0; i < n; ++i) { current = std::max(current, a[i]); push(current); }
            current = n;
            for (int i = n-1; i >= 0; --i) { current = std::min(current, a[i]); suffix_a[i] = current; }
            for (int i = 0; i < n; ++i) push(suffix_a[i]);
            return code;
        };

        auto visit = [&](auto&& self, int i, uint64_t mult) -> void {
            if (i == n) {
                fibre[key()] += mult;
                represented_relations += mult;
                return;
            }
            for (const auto& type : row_types) {
                a[i] = type.min_target;
                b[i] = type.max_target;
                self(self, i+1, mult*type.multiplicity);
            }
        };
        visit(visit, 0, 1);
        uint64_t max_fibre=0, max_fibre_classes=0;
        for (const auto& [profile, size] : fibre) {
            if (size > max_fibre) { max_fibre=size; max_fibre_classes=1; }
            else if (size == max_fibre) ++max_fibre_classes;
        }
        if (represented_relations != (1ULL << (n*n))) return 2;
        std::cout << n << ' ' << fibre.size() << ' ' << represented_relations
                  << ' ' << max_fibre << ' ' << max_fibre_classes << '\n';
    }
}
