class Solution(object):
    def sieve_of_eratosthenes(self, n):
        if n < 2:
            return []
        
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, n + 1, i):
                    primes[multiple] = False

        return primes

    def closestPrimes(self, left, right):
        primes = self.sieve_of_eratosthenes(right)

        prime_list = [i for i in range(left, right + 1) if primes[i]]

        if len(prime_list) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        num1, num2 = -1, -1
        
        for i in range(len(prime_list) - 1):
            gap = prime_list[i + 1] - prime_list[i]
            if gap < min_gap:
                min_gap = gap
                num1, num2 = prime_list[i], prime_list[i + 1]

        return [num1, num2]

sol = Solution()
print("\nCase 1: 10, 19")
print(sol.closestPrimes(10, 19))
print("\nCase 2: 4, 6")
print(sol.closestPrimes(4, 6))
