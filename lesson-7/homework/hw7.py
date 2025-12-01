# 
1. is_prime(n) funksiyasi
is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
#
2. digit_sum(k) funksiyasi
digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    return sum(int(x) for x in str(k))
print(digit_sum(707))
#
3. Ikki sonning darajalari
Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def limit_square(n):
    result = []
    k = 0
    while k ** 2 < n:
        result.append(k ** 2)
        k += 1 
    return result
print(limit_square(10))
    
