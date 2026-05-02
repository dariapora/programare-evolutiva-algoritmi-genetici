### Cerințe

1. Fie 𝑓: 𝒫(𝑛) → ℕ 𝑝𝜖𝒫(𝑛), 𝑓(𝑝) = |{(𝑖, 𝑗) 𝑖 < 𝑗, 𝑝(𝑖) = 𝑗 ş𝑖 𝑝(𝑗) = 𝑖
⁄ }| funcţia obiectiv a unei
probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de
mutaţie prin inserare care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia
rezultată are tot dim indivizi.


2. Fie 𝑓: {1,2, … ,1500} × {−1,0, , … ,2500} → ℝ, 𝑓(𝑥, 𝑦) = 𝑦 ∗ (𝑠𝑖𝑛(𝑥 − 2))2 funcţia obiectiv a
unei probleme de maxim. Fiecărui fenotip (𝑥, 𝑦) ∈ {1,2, … ,1500} × {−1,0, , … ,2500} îi
corespunde un genotip şir binar obţinut prin reprezentarea în bază 2 a fiecărei componente a
fenotipului.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de încrucişare multi-punct pentru 3 puncte de încrucişare care, pe baza populaţiei pop
obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi
recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări
cromozomiale).

   
3. Fie 𝑓: [−1,1] × [0,0.2] × [0,1] × [0,5] → ℝ, 𝑓(𝑥1, 𝑥2, 𝑥3) = 1 + 𝑠𝑖𝑛(2𝑥1− 𝑥3) + (𝑥2 ∗
𝑥4)1
3 ⁄ funcţia obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥 =
(𝑥1, 𝑥2, 𝑥3, 𝑥4)𝑇
, 𝑥 ∈ [−1,1] × [0,0.2] × [0,1] × [0,5]
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie mutaţie de tip fluaj cu pragul 𝑡 =
0.6 (𝜎 = 𝑡) care, pe baza populaţiei pop obţine o nouă populaţie, cu indivizii eventual mutanţi ai
lui pop.


4. Fie 𝑓: [−1,1] × [0,1] × [−2,1] → ℝ, 𝑓(𝑥1, 𝑥2, 𝑥3) = 1 + 𝑠𝑖𝑛(2𝑥1− 𝑥3) + 𝑐𝑜𝑠(𝑥2) funcţia
obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥 = (𝑥1, 𝑥2, 𝑥3)𝑇
, 𝑥 ∈
[−1,1] × [0,1] × [−2,1]
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
indivizii populaţiei sunt însoţiţi de funcţia merit (sunt vectori cu 4 componente).
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de recombinare aritmetică totală care, pe baza populaţiei pop obţine o nouă populaţie,
popc. Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea
fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale).



5. Fie funcţia 𝑓(𝑥) = ∑ 𝑥𝑖
𝑖=1 , 𝑥 = (𝑥1, … , 𝑥7) ∈ {0,1}7 care trebuie maximizată (un genotip este
un vector binar cu 7 componente).
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de încrucişare multi-punct pentru 2 puncte de încrucişare care, pe baza populaţiei pop
obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi (este utilizată şi
recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări
cromozomiale)


6. Fie 𝑓: {1,2, … ,350} → ℝ, 𝑓(𝑥) = 𝑥2 funcţia obiectiv a unei probleme de maxim. Fiecărui
fenotip 𝑥 ∈ {1,2, … ,350} îi corespunde un genotip şir binar obţinut prin codificarea Gray.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b. Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând
operatorul de încrucişare uni-punct care, pe baza populaţiei pop obţine o nouă populaţie, popc.
Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată).


7. Fie 𝑓: 𝒫(𝑛) → ℕ 𝑝𝜖𝒫(𝑛), 𝑓(𝑝) = |{(𝑖, 𝑗) 𝑖 < 𝑗, 𝑝(𝑖) = 𝑗 ş𝑖 𝑝(𝑗) = 𝑖
⁄ }| funcţia obiectiv a unei
probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de
mutaţie prin amestec care, pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia
rezultată are tot dim indivizi.
𝑛−1


8. Fie 𝑓: 𝒫(𝑛) → ℕ funcţia obiectiv definită pentru problema celor n regine astfel:
𝑝𝜖𝒫(𝑛), 𝑓(𝑝) = 𝑛 ×
− |{(𝑖, 𝑗) 𝑖 < 𝑗, |𝑝(𝑖) − 𝑝(𝑗)| = |𝑖 − 𝑗|
⁄ }|, unde 𝒫(𝑛) desemnează
2
mulţimea permutărilor de n elemente.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1, pop2
cu câte dim indivizi. Scrieţi o funcţie Python care obţine o nouă populaţie prin aplicarea unei
proceduri de tip elitist celor două populaţii, unde pop2 este considerată populaţia progeniturilor lui
pop1. Populaţia rezultată are tot dim indivizi.


9. Fie 𝑓: {1,2, … ,2500} → ℝ, 𝑓(𝑥) = (𝑠𝑖𝑛(𝑥 − 2))2 funcţia obiectiv a unei probleme de maxim.
Fiecărui fenotip 𝑥 ∈ {1,2, … ,2500} îi corespunde un genotip şir binar obţinut prin reprezentarea
standard în bază 2 a lui x.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin
aplicarea selecţiei de tip ruletă cu distribuţia de probabilitate FPS cu sigma-scalare.


10. Fie 𝑓: {1,2, … ,350} → ℝ, 𝑓(𝑥) = 𝑥2 funcţia obiectiv a unei probleme de maxim. Fiecărui
fenotip 𝑥 ∈ {1,2, … ,350} îi corespunde un genotip şir binar obţinut prin codificarea Gray.
a. b. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1,
pop2. Scrieţi o funcţie Python care obţine o nouă populaţie prin aplicarea unei proceduri de tip
GENITOR (cu înlocuirea a 2 indivizi) celor două populaţii, unde pop2 este considerată populaţia
progeniturilor lui pop1. Populaţia rezultată are tot dim indivizi.

    
11. Fie 𝑓: {1,2, … ,500} → ℝ, 𝑓(𝑥) = (𝑠𝑖𝑛(𝑥 − 2))2
− 𝑥 ∙ 𝑐𝑜𝑠(2 ∙ 𝑥) funcţia obiectiv a unei
probleme de maxim. Fiecărui fenotip 𝑥 ∈ {1,2, … ,500} îi corespunde un genotip şir binar obţinut
prin reprezentarea standard în bază 2 a lui x.
a. Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b. Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin
aplicarea selecţiei de tip turneu cu k indivizi (k parametru de intrare).