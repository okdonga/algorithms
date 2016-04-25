#  '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

# Pseudocode :
# 1. keep two pointers in target and pattern as i and j
# 2. if target[i] == pattern[j] or target[i] == '?' keep moving
# 3. if '*' exists in pattern, mark j in pattern as star, i in target as s_star
# 4. Loop until target[i] == pattern[star+1]

def isMatch(target, pattern):
  i = 0
  j = 0
  star = -1
  s_star = 0
  target_len = len(target)
  pattern_len = len(pattern)
  while i < target_len:
    if j < pattern_len and (pattern[j] == target[i] or pattern[j] == '?'):
      i += 1
      j += 1
    elif j < pattern_len and pattern[j] == '*':
      star = j
      s_star = i
      j += 1
    elif star !=  -1:
      j = star + 1
      s_star += 1
      i = s_star
    else:
      return False

  while j < pattern_len and pattern[j] == '*':
    j += 1
  return j == pattern_len

