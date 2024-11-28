def manacher_algorithm(s):
    # Preprocess the string
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0

    for i in range(1, n-1):
        mirror = 2*c - i
        if i < r:
            p[i] = min(r - i, p[mirror])

        # Expand around center i
        while i + (1 + p[i]) < n and i - (1 + p[i]) >= 0 and t[i + (1 + p[i])] == t[i - (1 + p[i])]:
            p[i] += 1

        # Update center and right boundary
        if i + p[i] > r:
            c, r = i, i + p[i]

    return p

def generate_palindrome_substrings(s):
    p = manacher_algorithm(s)
    palindromes = set()
    n = len(s)

    for i in range(len(p)):
        center = i // 2
        length = p[i]

        if i % 2 == 0:  # Odd-length palindromes
            start = center - length // 2
            end = center + length // 2
        else:  # Even-length palindromes
            start = center - (length - 1) // 2
            end = center + length // 2

        if 0 <= start < end <= n:
            palindromes.add(s[start:end])

    return list(palindromes)

# Test karne ke liye
input_string = "faisal"
result = generate_palindrome_substrings(input_string)
print(f"Input string: {input_string}")
print(f"Palindrome substrings: {result}")
