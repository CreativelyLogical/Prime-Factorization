# This program is intended to help the user find 
# the 2 distinct prime factors of an inputted integer


def isPrime(n):
	if (n == 1 or n == 2 or n == 3):
		return True
	elif n > 3:
		for i in range(2, n):
			if n % i == 0:
				return False
			else:
				continue
	return True



n = input("Please enter your input..\n")


p = 0
q = 0

ans_found = False

for i in range(2, n):
	if isPrime(i):
		for j in range(0, n):
			if isPrime(j):
				if i * j == n:
					p = i
					q = j
					ans_found = True
					break
	if (ans_found == True):
		break

print("The prime factorization of {} is {} and {}".format(n, p, q))








