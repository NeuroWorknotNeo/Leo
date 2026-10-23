# Q3. Классическая теория поля — диагностика

> **Код в плане:** [Q3](../../PLAN.md#q3) · **Время:** ≈ 200 минут ([расширенный экзамен](../../README.md#physics)) · **Максимум:** 100 баллов · **Этап плана:** 4
>
> **Требует:** Q1, G2; R7 желательно. **Можно пользоваться:** только бумагой и ручкой (никаких книг, конспектов, интернета, CAS).

## Как проходить

1. Засечь 200 минут или сдавать в два захода: части A–C (120 минут), затем D–E (80 минут); подробнее — в [особых правилах для физики](../../README.md#physics). Ориентировочное время на части указано в заголовках; переходить к следующей части можно в любой момент.
2. Писать решения полностью, как на письменном экзамене. «Понятно, как делать» без записи — 0 баллов.
3. Ключ в конце файла открывать только после окончания времени. Проверять себя строго, по критериям из ключа.
4. Записать баллы по частям в таблицу результатов в конце и прочитать интерпретацию.

Соглашения: поля классические, $`c=1`$. В $`\mathbb{R}^{1,3}`$ метрика $`\eta=\mathrm{diag}(1,-1,-1,-1)`$, $`x^0=t`$, индексы поднимаются с помощью $`\eta`$, $`\Box=\partial_t^2-\Delta`$. Евклидово $`\mathbb{R}^4`$ ориентировано формой $`dx^0\wedge dx^1\wedge dx^2\wedge dx^3`$, $`\ast`$ — звёздочка Ходжа. Группа $`G\subset U(n)`$ компактна, $`\mathfrak{g}`$ — антиэрмитовы матрицы, $`\langle X,Y\rangle=-\mathrm{tr}(XY)`$. Связность в локальной тривиализации — $`\mathfrak{g}`$-значная 1-форма $`A`$, $`F_A=dA+A\wedge A`$, калибровочное преобразование $`A^g=g^{-1}Ag+g^{-1}dg`$, $`D_A=d+[A,\cdot\,]`$ на формах со значениями в $`\mathrm{ad}\,P`$. Для риманова 4-многообразия $`M`$

```math
S_{YM}(A)=-\int_M\mathrm{tr}(F_A\wedge\ast F_A)=\int_M\lvert F_A\rvert^2d\mathrm{vol},\qquad k(A)=-\frac{1}{8\pi^2}\int_M\mathrm{tr}(F_A\wedge F_A)
```

(для $`SU(2)`$-расслоения над компактным $`M`$ имеем $`k=-c_2(P)[M]`$). Электромагнитное поле (заряд и $`\hbar`$ равны $`1`$) — $`U(1)`$-связность $`\nabla=d-ia`$, $`a`$ — вещественная 1-форма, $`f=da`$; калибровочные преобразования $`\psi\mapsto e^{i\lambda}\psi`$, $`a\mapsto a+d\lambda`$ ($`e^{i\lambda}`$ — гладкая функция в $`U(1)`$); голономия по петле $`\gamma`$ равна $`\exp\left(i\oint_\gamma a\right)`$.

## Часть A. Определения и формулировки (≈ 30 мин, 20 баллов)

Дать точные определения / сформулировать теоремы полностью, со всеми условиями. 10 пунктов по 2 балла.

1. Лагранжева теория поля: поля — сечения расслоения $`E\to M`$, лагранжиан $`L(x,\phi,\partial\phi)`$. Что такое критическая точка действия на некомпактном $`M`$ (какие вариации допускаются); уравнения Эйлера–Лагранжа.
2. Теорема Нётер для теории поля: симметрия, ток, закон сохранения. При каких условиях заряд $`Q(t)=\int_{\mathbb{R}^3}j^0(t,x)d^3x`$ не зависит от $`t`$?
3. Канонический тензор энергии-импульса (откуда он берётся, в каком смысле сохраняется) и метрический $`T_{\mu\nu}=\frac{2}{\sqrt{\lvert g\rvert}}\frac{\delta S}{\delta g^{\mu\nu}}`$ (для каких теорий определён, почему симметричен и сохраняется). Какое свойство действия гарантирует $`T^\mu{}_\mu=0`$ на решениях?
4. Уравнения Клейна–Гордона и Дирака: лагранжианы, уравнения, соотношения на $`\gamma^\mu`$. Почему компоненты решения уравнения Дирака удовлетворяют уравнению Клейна–Гордона? Ток симметрии $`\psi\mapsto e^{i\alpha}\psi`$ и знак $`j^0`$ (сравнить с комплексным полем Клейна–Гордона).
5. Связность на главном $`G`$-расслоении (как форма на $`P`$ и локально), кривизна, калибровочная группа и её действие на пространстве связностей $`\mathcal{A}(P)`$, ковариантная производная на $`P\times_\rho V`$. Тождество Бьянки.
6. Электродинамика как теория $`U(1)`$-связности: какие уравнения Максвелла — тождество Бьянки, а какие — уравнения Эйлера–Лагранжа (с внешним током $`j^\mu`$); почему калибровочная инвариантность требует $`\partial_\mu j^\mu=0`$. Плоские $`U(1)`$-связности на связном $`X`$ с точностью до калибровки; эффект Ааронова–Бома в этих терминах.
7. Автодуальные и антиавтодуальные 2-формы и связности в размерности $`4`$; почему $`\Lambda^\pm`$ и $`S_{YM}`$ зависят только от конформного класса метрики. Инстантон на $`\mathbb{R}^4`$; теорема Уленбек об устранимой особенности и следствие для $`k(A)`$.
8. Топологический заряд солитона: вакуумное многообразие, конфигурации конечной энергии в размерности $`d=1,2,3`$ (кинки, вихри, монополи) — в какой гомотопической группе лежит заряд и почему он сохраняется. Сохраняющийся ток кинка теории $`\phi^4`$.
9. Черн–Вейль для $`U(1)`$- и $`SU(2)`$-расслоений: формулы для $`c_1`$, $`c_2`$, независимость от связности. Форма Черна–Саймонса как трансгрессия: $`\mathrm{tr}(F_A\wedge F_A)=d(\dots)`$ в тривиализации.
10. Пространство решений уравнения Клейна–Гордона как симплектическое многообразие: какие решения, формула симплектической формы, почему она не зависит от $`t`$, связь с каноническими переменными $`(\phi,\partial_t\phi)`$. Что меняется для калибровочных теорий?

## Часть B. Верно или неверно? (≈ 25 мин, 15 баллов)

Для каждого утверждения ответить «верно» или «неверно» и **обосновать**: короткое доказательство или контрпример. Ответ без обоснования — 0 баллов. 5 пунктов по 3 балла.

1. Пусть $`\psi`$ — комплекснозначное (не грассманово) решение уравнения $`(i\gamma^\mu\partial_\mu-m)\psi=0`$, $`m>0`$, $`\psi(t,\cdot)\in\mathcal{S}(\mathbb{R}^3;\mathbb{C}^4)`$, $`\psi\not\equiv0`$. Тогда энергия $`H=\int T^{00}d^3x`$ (канонический тензор лагранжиана $`\bar\psi(i\gamma^\mu\partial_\mu-m)\psi`$) положительна.
2. Если $`M`$ — компактное ориентированное риманово 4-многообразие, то всякая связность Янга–Миллса ($`D_A\ast F_A=0`$) на главном $`SU(2)`$-расслоении над $`M`$ автодуальна или антиавтодуальна.
3. Пусть $`d\ge2`$, $`V\colon\mathbb{R}^n\to[0,\infty)`$ гладкая, $`\phi\colon\mathbb{R}^d\to\mathbb{R}^n`$ — решение $`\Delta\phi=\nabla V(\phi)`$ с $`E(\phi)=\int\left(\frac12\lvert\nabla\phi\rvert^2+V(\phi)\right)d^dx<\infty`$. Тогда $`\phi`$ постоянно.
4. Действие $`\frac12\int\partial_\mu\phi\partial^\mu\phi\,d^4x`$ в $`\mathbb{R}^{1,3}`$ инвариантно относительно $`\phi(x)\mapsto\lambda\phi(\lambda x)`$. Поэтому его метрический тензор энергии-импульса (из $`\frac12\int g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi\sqrt{\lvert g\rvert}d^4x`$ при $`g=\eta`$) бесследов на решениях.
5. Всякое решение уравнения $`\phi''=\sin\phi`$ на $`\mathbb{R}`$ с $`\int\left(\frac12\phi'^2+1-\cos\phi\right)dx<\infty`$ имеет пределы $`\phi(\pm\infty)`$, и $`N=\frac{\phi(+\infty)-\phi(-\infty)}{2\pi}\in\lbrace-1,0,1\rbrace`$.

## Часть C. Стандартные задачи (≈ 65 мин, 30 баллов)

Вычисления и рутинные доказательства, которые должен уверенно делать каждый, кто прошёл курс. 5 задач по 6 баллов.

**C1.** Сигма-модель. $`(\Sigma,h)`$ — ориентированная риманова поверхность, $`(X,g)`$ — риманово многообразие, $`E(\phi,h)=\frac12\int_\Sigma h^{ab}g_{ij}(\phi)\partial_a\phi^i\partial_b\phi^jd\mathrm{vol}_h`$. (а) Вывести уравнения Эйлера–Лагранжа через $`\Delta_h`$ и символы Кристоффеля $`g`$. (б) Пусть $`K`$ — поле Киллинга на $`X`$. Доказать, что $`j=g(K(\phi),d\phi)`$ — нётеровский ток (какой симметрии?) и $`d\ast j=0`$ на решениях. (в) Тензор $`T_{ab}`$ определён условием $`\frac{d}{ds}\big\rvert_{0}E(\phi,h_s)=\frac12\int T_{ab}\delta h^{ab}d\mathrm{vol}_h`$, $`\delta h^{ab}=\frac{d}{ds}\big\rvert_0h_s^{ab}`$. Найти $`T_{ab}`$, проверить $`h^{ab}T_{ab}=0`$ и объяснить это. Доказать, что в конформной координате $`z`$ для решения $`T_{zz}=g(\partial_z\phi,\partial_z\phi)`$ голоморфна.

**C2.** Кинк. $`L=\frac12\phi_t^2-\frac12\phi_x^2-V(\phi)`$ в $`\mathbb{R}^{1,1}`$, $`V=\frac\lambda4(\phi^2-v^2)^2`$, $`\lambda,v>0`$, $`E[\phi]=\int\left(\frac12\phi'^2+V(\phi)\right)dx`$. (а) Пусть $`\phi\in C^1(\mathbb{R})`$, $`E[\phi]<\infty`$ и пределы $`\phi(\pm\infty)`$ существуют. Доказать, что они равны $`\pm v`$ и $`E[\phi]\ge\lvert W(\phi(+\infty))-W(\phi(-\infty))\rvert`$, $`W(\phi)=\sqrt{\lambda/2}\left(v^2\phi-\phi^3/3\right)`$. Когда равенство? (б) Найти все статические решения конечной энергии с $`\phi(\mp\infty)=\mp v`$ и их энергию $`M`$. (в) Для кинка $`\phi_K`$ и $`\mathcal{L}=-\frac{d^2}{dx^2}+V''(\phi_K)`$ доказать $`\mathcal{L}\phi_K'=0`$, объяснить смысл этого нулевого вектора и вывести $`\mathcal{L}\ge0`$ на $`L^2(\mathbb{R})`$.

**C3.** Ааронов–Бом и монополь Дирака. (а) На $`X=\mathbb{R}^3\setminus\lbrace x^1=x^2=0\rbrace`$ пусть $`a=\frac{\Phi}{2\pi}d\theta`$ ($`\theta`$ — полярный угол в плоскости $`x^1x^2`$). Найти $`f`$ и голономию по петле вокруг оси. Доказать, что $`a`$ калибровочно эквивалентна $`0`$ тогда и только тогда, когда $`\Phi\in2\pi\mathbb{Z}`$. (б) На $`Y=\mathbb{R}^3\setminus\lbrace0\rbrace`$ пусть $`f=\frac m2\sin\theta\,d\theta\wedge d\varphi`$ (сферические координаты). Проверить $`df=0`$, найти $`\int_{S^2}f`$ и доказать, что при $`m\neq0`$ нет 1-формы $`a`$ на $`Y`$ с $`da=f`$. (в) Найти $`a_N=c_N(1-\cos\theta)d\varphi`$, $`a_S=c_S(1+\cos\theta)d\varphi`$ с $`da_{N,S}=f`$, гладкие соответственно вне отрицательной и вне положительной полуоси $`x^3`$. Доказать, что они калибровочно эквивалентны на пересечении областей тогда и только тогда, когда $`m\in\mathbb{Z}`$, и что тогда $`c_1`$ полученного расслоения на $`S^2`$ равен $`m`$.

**C4.** Черн–Саймонс. $`Y`$ — замкнутое ориентированное 3-многообразие, $`A\in\Omega^1(Y;\mathfrak{su}(2))`$, $`g\in C^\infty(Y,SU(2))`$,

```math
\mathrm{cs}(A)=\frac{1}{8\pi^2}\int_Y\mathrm{tr}\left(A\wedge dA+\frac23A\wedge A\wedge A\right),\qquad w(g)=\frac{1}{24\pi^2}\int_Y\mathrm{tr}\left((g^{-1}dg)^3\right)\in\mathbb{Z}
```

(целочисленность $`w`$ можно не доказывать). (а) Доказать, что $`\frac{d}{dt}\big\rvert_0\mathrm{cs}(A+tb)=\frac{1}{4\pi^2}\int_Y\mathrm{tr}(b\wedge F_A)`$, найти критические точки. (б) Доказать $`\mathrm{cs}(A^g)=\mathrm{cs}(A)-w(g)`$. (в) Вывести, что при $`\ell\in\mathbb{Z}`$ величина $`e^{2\pi i\ell\,\mathrm{cs}(A)}`$ калибровочно инвариантна, а $`\mathrm{cs}`$ инвариантен относительно $`g`$, гомотопных постоянному.

**C5.** Поле Максвелла. $`S=\int\left(-\frac14f_{\mu\nu}f^{\mu\nu}-a_\mu j^\mu\right)d^4x`$, $`j^\mu`$ — внешний ток; $`E_i=f_{0i}`$, $`B_i=-\frac12\varepsilon_{ijk}f_{jk}`$. (а) Вывести уравнения Эйлера–Лагранжа. (б) При $`j=0`$ найти канонический тензор $`T_{\mathrm{can}}^{\mu\nu}`$; показать, что он не калибровочно инвариантен и, вообще говоря, не симметричен; доказать, что на решениях

```math
T_{\mathrm{can}}^{\mu\nu}-\partial_\lambda\left(f^{\lambda\mu}a^\nu\right)=T^{\mu\nu}:=-f^{\mu\lambda}f^{\nu}{}_{\lambda}+\frac14\eta^{\mu\nu}f_{\alpha\beta}f^{\alpha\beta},
```

и что $`T`$ и $`T_{\mathrm{can}}`$ дают одинаковые $`P^\nu=\int T^{0\nu}d^3x`$ (при каком убывании?). (в) Выразить $`T^{00}`$, $`T^{0i}`$ через $`E,B`$, найти $`T^\mu{}_\mu`$ и $`\partial_\mu T^{\mu\nu}`$ при $`j\neq0`$. Смысл компоненты $`\nu=0`$?

## Часть D. Ключевые доказательства (≈ 40 мин, 20 баллов)

Доказать центральные теоремы курса. Сюда входит контрольная точка из plan.md. 2 задачи по 10 баллов.

Контрольная точка состоит из трёх пунктов, поэтому пометку несут обе задачи.

**D1.** *(контрольная точка)* Уравнения Янга–Миллса и оценка Богомольного. $`M`$ — компактное ориентированное риманово 4-многообразие без края, $`P\to M`$ — главное $`SU(2)`$-расслоение; независимость $`k`$ от связности можно не доказывать.

(а) Доказать $`F_{A+tb}=F_A+tD_Ab+t^2b\wedge b`$ для $`b\in\Omega^1(M;\mathrm{ad}\,P)`$ и вывести: $`A`$ — критическая точка $`S_{YM}`$ тогда и только тогда, когда $`D_A\ast F_A=0`$. Записать уравнения в координатах на $`\mathbb{R}^4`$.

(б) Доказать тождество Бьянки $`D_AF_A=0`$.

(в) Доказать $`S_{YM}(A)\ge8\pi^2\lvert k(P)\rvert`$, причём равенство равносильно $`F_A=\ast F_A`$ при $`k\ge0`$ и $`F_A=-\ast F_A`$ при $`k\le0`$.

(г) Вывести, что (анти)автодуальные связности — решения уравнений Янга–Миллса и точки абсолютного минимума $`S_{YM}`$ на $`\mathcal{A}(P)`$. Каков знак $`k`$ для автодуальной связности с $`F_A\neq0`$?

**D2.** *(контрольная точка)* Инстантон BPST. $`\mathbb{R}^4=\mathbb{H}`$, $`x=x^0+x^1i+x^2j+x^3k`$, $`SU(2)=Sp(1)`$, $`\mathfrak{su}(2)=\mathrm{Im}\,\mathbb{H}`$, $`\mathrm{tr}\,q=2\,\mathrm{Re}\,q`$ (стандартное вложение $`\mathbb{H}\subset M_2(\mathbb{C})`$). $`\mathbb{H}`$-значные формы перемножаются через $`\wedge`$ и умножение кватернионов, $`dx=dx^0+i\,dx^1+j\,dx^2+k\,dx^3`$, $`\mathrm{Im}\,q=\frac12(q-\bar q)`$. При $`\rho>0`$

```math
A=\mathrm{Im}\left(\frac{x\,d\bar x}{\rho^2+\lvert x\rvert^2}\right).
```

(а) Доказать $`F_A=\dfrac{\rho^2\,dx\wedge d\bar x}{(\rho^2+\lvert x\rvert^2)^2}`$. Указание: для единичных $`p,q`$ замена $`x\mapsto px\bar q`$ переводит $`A`$ в $`pA\bar p`$, так что достаточно точек $`x=t\in\mathbb{R}`$.

(б) Разложив $`dx\wedge d\bar x`$ по $`dx^\mu\wedge dx^\nu`$, доказать, что $`A`$ автодуальна.

(в) Вычислить $`S_{YM}(A)`$ (со сходимостью) и доказать $`k(A)=1`$. Почему ответ не зависит от $`\rho`$?

## Часть E. Задачи повышенной сложности (≈ 40 мин, 15 баллов)

Нестандартные задачи: проверяют, умеете ли вы применять теорию там, где путь не подсказан. Не огорчайтесь, если не все решены. E1 — 7 баллов, E2 — 8 баллов.

**E1.** Вихри. На $`\mathbb{R}^2`$: $`a=a_jdx^j`$ вещественная, $`\phi\colon\mathbb{R}^2\to\mathbb{C}`$, $`D_j\phi=\partial_j\phi-ia_j\phi`$, $`f_{12}=\partial_1a_2-\partial_2a_1`$,

```math
E(a,\phi)=\frac12\int_{\mathbb{R}^2}\left(f_{12}^2+\lvert D_1\phi\rvert^2+\lvert D_2\phi\rvert^2+\frac14\left(1-\lvert\phi\rvert^2\right)^2\right)d^2x .
```

Пусть $`E<\infty`$, $`f_{12}\in L^1`$ и равномерно $`\lvert\phi\rvert\to1`$, $`\lvert x\rvert\lvert D\phi\rvert\to0`$ при $`\lvert x\rvert\to\infty`$. (а) Доказать $`\int f_{12}=2\pi N`$, где $`N`$ — степень $`\phi/\lvert\phi\rvert`$ на больших окружностях (обход против часовой стрелки). (б) Доказать $`E\ge\pi\lvert N\rvert`$; при $`N\ge0`$ равенство равносильно $`D_1\phi+iD_2\phi=0`$, $`f_{12}=\frac12(1-\lvert\phi\rvert^2)`$. Указание: $`\lvert D_1\phi\rvert^2+\lvert D_2\phi\rvert^2=\lvert D_1\phi+iD_2\phi\rvert^2+f_{12}\lvert\phi\rvert^2+\partial_1J_2-\partial_2J_1`$, $`J_k=\mathrm{Im}(\bar\phi D_k\phi)`$. (в) Почему рассуждение B3 не запрещает вихри? Как ведут себя слагаемые $`E`$ при $`a\mapsto\lambda a_j(\lambda x)dx^j`$, $`\phi\mapsto\phi(\lambda x)`$? Вывести (на физическом уровне строгости) для решений $`\int f_{12}^2=\frac14\int(1-\lvert\phi\rvert^2)^2`$.

**E2.** Заряд инстантона как степень. Пусть $`A`$ — $`SU(2)`$-связность на $`\mathbb{R}^4`$, и $`A=g^{-1}dg`$ при $`\lvert x\rvert\ge R_0`$. Для $`h\colon S^3_R\to SU(2)`$ положим $`w(h)=\frac{1}{24\pi^2}\int_{S^3_R}\mathrm{tr}\left((h^{-1}dh)^3\right)`$ (ориентация — как у границы шара). (а) Доказать $`\mathrm{tr}(F_A\wedge F_A)=d\,\mathrm{tr}\left(A\wedge dA+\frac23A^3\right)`$. (б) Доказать $`k(A)=w(g\rvert_{S^3_R})`$ при $`R\ge R_0`$. (в) Доказать, что $`w`$ — гомотопический инвариант. (г) Вычислить $`w(g)`$ для $`g(x)=\bar x/\lvert x\rvert`$ (обозначения D2) и объяснить, почему для инстантона BPST $`k=w(g)`$, хотя он не равен $`g^{-1}dg`$ ни при каком $`R_0`$.

## Карта навыков

| Тема из «Содержания» | Задачи |
|---|---|
| Лагранжева теория поля, уравнения Эйлера–Лагранжа | A1, C1, C2, C5, D1 |
| Теорема Нётер, тензор энергии-импульса | A2, A3, B1, B4, C1, C5 |
| Уравнения Клейна–Гордона и Дирака как классические поля | A4, A10, B1 |
| Электродинамика как U(1)-связность, калибровочная инвариантность, Ааронов–Бом | A5, A6, C3, C5 |
| Уравнения Янга–Миллса | A5, A7, B2, D1 |
| Инстантоны, топологический заряд, оценка Богомольного, BPST (контрольная точка) | A7, A9, D1, D2, E2 |
| Солитоны: кинки, вихри, монополи | A8, B3, B5, C2, C3, E1 |
| Функционал Черна–Саймонса | A9, C4, E2 |
| Пространство решений как симплектическое многообразие | A10 |

Если по теме потеряно больше половины баллов — к ней стоит вернуться:
- лагранжев формализм, Нётер, тензор энергии-импульса — Ландау, Лифшиц, т. 2, §§ 32–33 и § 94; Deligne, Freed «Classical field theory» (Quantum Fields and Strings, т. 1);
- поля Клейна–Гордона и Дирака — Folland «Quantum Field Theory: A Tourist Guide for Mathematicians», глава об уравнении Дирака;
- электродинамика, Ааронов–Бом, монополь Дирака — Ландау, Лифшиц, т. 2, §§ 26–31; Naber «Topology, Geometry and Gauge Fields: Foundations» (монополь Дирака и расслоение Хопфа);
- связности, Янг–Миллс, инстантоны — Bleecker «Gauge Theory and Variational Principles»; Atiyah «Geometry of Yang–Mills Fields»; Donaldson, Kronheimer «The Geometry of Four-Manifolds», гл. 2–3; Рубаков, главы об инстантонах;
- солитоны — Manton, Sutcliffe «Topological Solitons», гл. 4 (теорема Деррика), 5, 7, 8; Jaffe, Taubes «Vortices and Monopoles»; Рубаков, главы о солитонах;
- Черн–Саймонс, Черн–Вейль — Freed «Classical Chern–Simons theory, Part 1» (Adv. Math., 1995); Milnor, Stasheff «Characteristic Classes», приложение C;
- симплектическая структура на решениях — Crnković, Witten «Covariant description of canonical formalism in geometrical theories» (1987).

## Результаты и интерпретация

| Часть | Максимум | Мои баллы |
|---|---|---|
| A. Определения | 20 | |
| B. Верно/неверно | 15 | |
| C. Стандартные задачи | 30 | |
| D. Ключевые доказательства | 20 | |
| E. Повышенная сложность | 15 | |
| **Итого** | **100** | |

| Баллы | Уровень | Что делать |
|---|---|---|
| 0–39 | Не усвоено | Проверить пререквизиты: части A и C диагностик Q1 и G2 (желательно и R7); затем Рубаков, ч. I, и Ландау–Лифшиц, т. 2, гл. III–IV, переводя всё на язык связностей по Bleecker |
| 40–59 | Фрагментарно | По карте навыков выбрать провальные темы; прорешать задачи Ландау–Лифшица к §§ 32–33 и провести вычисления Manton–Sutcliffe, гл. 4, 5, 7 |
| 60–74 | Рабочий уровень | Можно начинать Q4 и Q7, закрывая пробелы; для Q4 критичны Нётер, поля Клейна–Гордона и Дирака, для Q7 — метрический тензор энергии-импульса |
| 75–89 | Уверенно | Можно ставить галочку в plan.md |
| 90–100 | Свободное владение | Переходить к Q4 и Q7; калибровочные теории и инстантоны ведут к G9 и V6: Atiyah «Geometry of Yang–Mills Fields», Donaldson–Kronheimer (модули антиавтодуальных связностей, ADHM), Freed о теории Черна–Саймонса |

**Правило галочки:** ставить `[x]` напротив Q3 в plan.md, если итог ≥ 75, в каждой из частей A–D набрано не меньше половины баллов, а задачи с пометкой «контрольная точка» (D1 и D2) решены полностью.

**Диагностика по профилю:**
- A высокое, C низкое — язык расслоений выучен, но нет навыка счёта: прорешать тензоры энергии-импульса (Ландау–Лифшиц, §§ 32–33), кинки и вихри (Manton–Sutcliffe, гл. 5, 7), монополь Дирака в двух картах.
- C высокое, D низкое — не работает геометрия связностей: повторить G2 (ковариантный дифференциал, Бьянки, интегрирование по частям для $`\mathrm{ad}\,P`$-значных форм) и восстановить D1, D2 по Atiyah.
- Низкие B1 и B4 — смешиваются симметрии и свойства тензора энергии-импульса: разобрать канонический и метрический тензоры, «улучшение» и неограниченность энергии классического поля Дирака (к ней вернётся Q4).
- E = 0 при остальном ≥ 75 — нормально: вихри и связь заряда инстантона со степенью $`S^3\to SU(2)`$ встретятся на пути к G9 и V6.

## Ключ для самопроверки

<details>
<summary>Открыть только после окончания экзамена</summary>

### Часть A

1. Лагранжиан — функция на 1-струях $`J^1E`$ со значениями в плотностях. Действие $`\int_KL`$ рассматривается на компактах $`K`$; $`\phi`$ — критическая точка, если $`\frac{d}{ds}\big\rvert_0\int_KL(\phi_s)=0`$ для всех вариаций с носителем в компакте $`K`$. Это равносильно $`\frac{\partial L}{\partial\phi^a}-\partial_\mu\frac{\partial L}{\partial(\partial_\mu\phi^a)}=0`$ (интегрирование по частям, основная лемма; граничные условия не нужны).
2. Если $`\delta\phi^a=\varepsilon X^a(x,\phi)`$ и $`\delta L=\varepsilon\partial_\mu K^\mu`$ тождественно (для всех полей), то $`j^\mu=\frac{\partial L}{\partial(\partial_\mu\phi^a)}X^a-K^\mu`$ удовлетворяет $`\partial_\mu j^\mu=0`$ на решениях. $`Q`$ сохраняется, если $`j^0(t,\cdot)\in L^1`$ и поток $`j`$ через большие сферы стремится к нулю (например, $`j(t,\cdot)`$ с компактным носителем — для финитных данных Коши по конечности скорости распространения — или $`\lvert j\rvert=o(\lvert x\rvert^{-2})`$ равномерно по $`t`$ на отрезках). Обязательно: «с точностью до полной производной», формула, условие убывания.
3. $`T^\mu{}_\nu=\frac{\partial L}{\partial(\partial_\mu\phi^a)}\partial_\nu\phi^a-\delta^\mu_\nu L`$ — ток Нётер трансляций (для $`L`$ без явной зависимости от $`x`$), $`\partial_\mu T^\mu{}_\nu=0`$ на решениях; может быть несимметричным и калибровочно неинвариантным, исправляется добавкой $`\partial_\lambda B^{\lambda\mu\nu}`$, $`B^{\lambda\mu\nu}=-B^{\mu\lambda\nu}`$ (Белинфанте). Метрический тензор определён для теорий $`S[g,\phi]`$ на произвольной метрике; симметричен, $`\nabla^\mu T_{\mu\nu}=0`$ на решениях из инвариантности относительно диффеоморфизмов; в плоском пределе совпадает с тензором Белинфанте. Если $`S[e^{2\sigma}g,e^{w\sigma}\phi]=S[g,\phi]`$ (вейлевская инвариантность), то $`T^\mu{}_\mu=0`$ на решениях.
4. КГ: $`L=\frac12\partial_\mu\phi\partial^\mu\phi-\frac12m^2\phi^2`$, $`(\Box+m^2)\phi=0`$. Дирак: $`\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2\eta^{\mu\nu}`$, $`(\gamma^\mu)^{\ast}=\gamma^0\gamma^\mu\gamma^0`$, $`\bar\psi=\psi^{\ast}\gamma^0`$, $`L=\bar\psi(i\gamma^\mu\partial_\mu-m)\psi`$, $`(i\gamma^\mu\partial_\mu-m)\psi=0`$. Умножая на $`(i\gamma^\nu\partial_\nu+m)`$: $`-(\Box+m^2)\psi=0`$. Ток $`\bar\psi\gamma^\mu\psi`$, $`j^0=\psi^{\ast}\psi\ge0`$; у комплексного КГ $`j^\mu=i(\bar\phi\partial^\mu\phi-\phi\partial^\mu\bar\phi)`$, $`j^0`$ знакопеременно.
5. Связность — $`\omega\in\Omega^1(P;\mathfrak{g})`$, $`\omega(\xi^\sharp)=\xi`$, $`R_h^{\ast}\omega=\mathrm{Ad}_{h^{-1}}\omega`$; кривизна $`d\omega+\frac12[\omega\wedge\omega]`$ горизонтальна и эквивариантна, $`F\in\Omega^2(M;\mathrm{ad}\,P)`$. Локально $`A=s^{\ast}\omega`$, $`F=dA+A\wedge A`$; при $`s'=sg`$: $`A'=g^{-1}Ag+g^{-1}dg`$, $`F'=g^{-1}Fg`$. $`\mathcal{G}=\mathrm{Aut}_M(P)=\Gamma(P\times_{\mathrm{conj}}G)`$ действует на аффинном $`\mathcal{A}(P)`$ (модель $`\Omega^1(M;\mathrm{ad}\,P)`$). $`D_A\psi=d\psi+\rho_{\ast}(A)\psi`$. Бьянки: $`D_AF_A=0`$.
6. $`df=0`$ (то есть $`\mathrm{div}\,B=0`$, $`\partial_tB+\mathrm{rot}\,E=0`$) — тождество Бьянки; $`\partial_\mu f^{\mu\nu}=j^\nu`$ — уравнения Эйлера–Лагранжа. При $`a\mapsto a+d\lambda`$ действие меняется на $`\int\lambda\partial_\mu j^\mu`$ — инвариантность для всех финитных $`\lambda`$ равносильна $`\partial_\mu j^\mu=0`$. Плоские связности на связном $`X`$ по модулю калибровки $`\leftrightarrow\mathrm{Hom}(\pi_1(X),U(1))`$ (голономия). Ааронов–Бом: вне соленоида $`f=0`$, но голономия $`e^{i\Phi}`$ наблюдаема — физически значима связность, а не только $`f`$.
7. В размерности $`4`$ $`\ast^2=1`$ на $`\Lambda^2`$, $`\Lambda^\pm`$ — собственные подпространства, ортогональные, ранга $`3`$. Автодуальность: $`F=\ast F`$, антиавтодуальность: $`F=-\ast F`$. При $`g\mapsto e^{2\sigma}g`$ звёздочка на $`p`$-формах умножается на $`e^{(n-2p)\sigma}=1`$, поэтому $`\Lambda^\pm`$ и $`-\mathrm{tr}(F\wedge\ast F)`$ конформно инвариантны. Инстантон — (анти)автодуальная связность на $`\mathbb{R}^4`$ с $`S_{YM}<\infty`$. Уленбек: связность Янга–Миллса на $`\mathbb{R}^4=S^4\setminus\lbrace\mathrm{pt}\rbrace`$ с конечным действием после калибровки продолжается до гладкой связности на расслоении над $`S^4`$, поэтому $`k\in\mathbb{Z}`$.
8. $`\mathcal{V}=V^{-1}(0)`$ ($`V\ge0`$; в калибровочной теории — по модулю калибровки). Конечность энергии загоняет поле на бесконечности в $`\mathcal{V}`$; заряд — класс отображения $`S^{d-1}_\infty\to\mathcal{V}`$: $`d=1`$ — пара $`(\phi(-\infty),\phi(+\infty))`$ ($`\pi_0`$); $`d=2`$, $`\mathcal{V}=S^1`$ — число вихрей в $`\pi_1(S^1)=\mathbb{Z}`$ (поток$`/2\pi`$); $`d=3`$, $`\mathcal{V}=SU(2)/U(1)=S^2`$ — магнитный заряд в $`\pi_2(S^2)`$ (для монополя Дирака — $`c_1`$ на $`S^2_\infty`$). Дискретный инвариант не меняется при непрерывной эволюции в классе конечной энергии. Кинк: $`j^\mu=\frac{1}{2v}\varepsilon^{\mu\nu}\partial_\nu\phi`$, $`\partial_\mu j^\mu=0`$ тождественно, $`Q=\frac{\phi(+\infty)-\phi(-\infty)}{2v}`$.
9. $`\det\left(1+\frac{i}{2\pi}F\right)=1+c_1+c_2+\dots`$ — замкнутые формы, классы не зависят от связности и целочисленны. Для $`\nabla=d-ia`$: $`c_1=[f/2\pi]`$, $`\int_\Sigma f\in2\pi\mathbb{Z}`$; для $`SU(2)`$: $`c_2=\left[\frac{1}{8\pi^2}\mathrm{tr}(F\wedge F)\right]`$. При $`A_t=A_0+tb`$: $`\frac{d}{dt}\mathrm{tr}(F_t\wedge F_t)=2\,\mathrm{tr}(D_{A_t}b\wedge F_t)=d\left(2\,\mathrm{tr}(b\wedge F_t)\right)`$ (Бьянки) — трансгрессия. Локально $`\mathrm{tr}(F\wedge F)=d\,\mathrm{tr}\left(A\wedge dA+\frac23A^3\right)`$.
10. Вещественные решения с пространственно компактным носителем; $`\phi\mapsto(\phi,\partial_t\phi)\rvert_{t=0}`$ — биекция на $`C_c^\infty(\mathbb{R}^3)^2`$. $`\Omega(\phi_1,\phi_2)=\int(\phi_1\partial_t\phi_2-\phi_2\partial_t\phi_1)d^3x`$; ток $`\phi_1\partial^\mu\phi_2-\phi_2\partial^\mu\phi_1`$ сохраняется, поэтому $`\Omega`$ не зависит от $`t`$. В данных Коши $`\Omega=\int\delta\phi\wedge\delta\pi`$, $`\pi=\partial_t\phi`$, эволюция — гамильтонов поток $`H=\frac12\int(\pi^2+\lvert\nabla\phi\rvert^2+m^2\phi^2)`$. В калибровочных теориях $`\Omega`$ вырождена вдоль калибровочных орбит: фазовое пространство — симплектическая редукция (связь — закон Гаусса).

### Часть B

1. **Неверно.** $`T^{00}=i\psi^{\ast}\partial_t\psi-L`$, на решениях $`L=0`$, а $`i\partial_t\psi=h\psi`$, $`h=-i\gamma^0\gamma^j\partial_j+\gamma^0m`$; значит, $`H=\langle\psi,h\psi\rangle_{L^2}`$. Символ $`\hat h(p)`$ эрмитов, $`\hat h(p)^2=E_p^2`$, $`E_p=\sqrt{\lvert p\rvert^2+m^2}`$, $`\mathrm{tr}\,\hat h=0`$, так что собственные значения $`\pm E_p`$. Данные $`\hat\psi(0,p)=\frac12\left(1-\hat h(p)/E_p\right)\hat\chi(p)\neq0`$, $`\chi\in\mathcal{S}`$, дают решение из $`\mathcal{S}`$ с $`H=-\int E_p\lvert\hat\psi\rvert^2d^3p<0`$. Положительность энергии появляется только при квантовании с антикоммутирующими полями (Q4).
2. **Неверно.** $`M=T^4=\mathbb{R}^4/\mathbb{Z}^4`$ (плоский), $`\omega=2\pi dx^1\wedge dx^2`$ — замкнутая форма с периодами в $`2\pi\mathbb{Z}`$, поэтому есть $`U(1)`$-расслоение $`L`$ со связностью $`d-ia`$, $`da=\omega`$ (прообраз расслоения степени $`1`$ на $`T^2`$). На $`SU(2)`$-расслоении $`L\oplus L^{-1}`$ связность $`A=\mathrm{diag}(-ia,ia)`$ имеет $`F_A=\mathrm{diag}(-i\omega,i\omega)`$ и $`D_A\ast F_A=0`$, так как $`\ast\omega=2\pi dx^3\wedge dx^4`$ замкнута; но $`\ast\omega\neq\pm\omega`$. Здесь $`k=0<S_{YM}=8\pi^2`$.
3. **Верно** (Деррик–Похожаев). Умножив уравнение на $`x\cdot\nabla\phi`$ и проинтегрировав по $`B_R`$:

<div align="center">

$`\displaystyle \frac{d-2}{2}\int_{B_R}\lvert\nabla\phi\rvert^2+d\int_{B_R}V(\phi)=R\int_{\partial B_R}\left(\frac12\lvert\nabla\phi\rvert^2-\lvert\partial_r\phi\rvert^2+V(\phi)\right)d\sigma .`$

</div>

Правая часть по модулю $`\le R\int_{\partial B_R}e`$, $`e=\frac12\lvert\nabla\phi\rvert^2+V`$, а $`\int_0^\infty\left(\int_{\partial B_R}e\right)dR=E<\infty`$, поэтому вдоль $`R_k\to\infty`$ она стремится к $`0`$: $`\frac{d-2}{2}\int\lvert\nabla\phi\rvert^2+d\int V=0`$. При $`d\ge3`$ отсюда $`\nabla\phi=0`$. При $`d=2`$: $`V(\phi)\equiv0`$, значения $`\phi`$ — точки минимума $`V`$, $`\nabla V(\phi)=0`$, $`\phi`$ гармонична с $`\nabla\phi\in L^2`$, и по теореме о среднем $`\lvert\partial_i\phi(x)\rvert\le(\pi R^2)^{-1/2}\lVert\partial_i\phi\rVert_{L^2}\to0`$. (При $`d=1`$ неверно — кинк.)
4. **Неверно.** $`T_{\mu\nu}=\partial_\mu\phi\partial_\nu\phi-\frac12\eta_{\mu\nu}(\partial\phi)^2`$, $`T^\mu{}_\mu=-(\partial\phi)^2`$; на решении $`\phi=t`$ след равен $`-1`$. Действие не вейлевски инвариантно; масштабная инвариантность даёт лишь $`T^\mu{}_\mu=-\frac12\Box(\phi^2)`$ на решениях, и бесследов «улучшенный» тензор $`T_{\mu\nu}-\frac16(\partial_\mu\partial_\nu-\eta_{\mu\nu}\Box)\phi^2`$ (конформная связь с $`R\phi^2`$). В размерности $`2`$ минимальная связь вейлевски инвариантна (C1).
5. **Верно.** $`\frac12\phi'^2-(1-\cos\phi)=c`$; при $`c>0`$ расходится $`\int\phi'^2`$, при $`c<0`$ — $`\int(1-\cos\phi)`$, значит, $`c=0`$, $`\phi'=\pm2\lvert\sin(\phi/2)\rvert`$. Если $`\phi(x_0)\in2\pi\mathbb{Z}`$, то по единственности $`\phi`$ постоянно, $`N=0`$. Иначе $`\phi`$ остаётся в $`(2\pi n,2\pi n+2\pi)`$ и строго монотонна, пределы существуют и (иначе $`\phi'\not\to0`$) лежат в $`2\pi\mathbb{Z}`$ — это концы интервала, $`N=\pm1`$. Решения: $`2\pi n+4\arctan e^{\pm(x-x_0)}`$, энергия $`8`$.

### Часть C

**C1.** (а) $`\Delta_h\phi^k+h^{ab}\Gamma^k_{ij}(\phi)\partial_a\phi^i\partial_b\phi^j=0`$, $`\Delta_h=\frac{1}{\sqrt h}\partial_a\left(\sqrt hh^{ab}\partial_b\right)`$ — гармонические отображения ($`\tau(\phi)=0`$). (б) Поток $`K`$ — изометрии $`X`$, $`E`$ инвариантна; ток $`j_a=g_{ij}K^i(\phi)\partial_a\phi^j`$. $`\nabla^aj_a=h^{ab}g(\nabla_{\partial_a\phi}K,\partial_b\phi)+g(K,\tau(\phi))`$: первое слагаемое $`0`$, так как $`g(\nabla_\cdot K,\cdot)`$ кососимметрична (Киллинг), второе — $`0`$ на решениях. (в) Из $`\delta\sqrt h=-\frac12\sqrt hh_{ab}\delta h^{ab}`$: $`T_{ab}=g(\partial_a\phi,\partial_b\phi)-\frac12h_{ab}\lvert d\phi\rvert^2`$, $`h^{ab}T_{ab}=0`$. Причина: $`\sqrt hh^{ab}`$ не меняется при $`h\mapsto e^{2\sigma}h`$ в размерности $`2`$ (вейлевская инвариантность), а $`\delta h^{ab}=-2\sigma h^{ab}`$. Так как $`h_{zz}=0`$, $`T_{zz}=g(\partial_z\phi,\partial_z\phi)`$; $`\Delta_h=4e^{-2\sigma}\partial_z\partial_{\bar z}`$, уравнение: $`\nabla_{\partial_{\bar z}}\partial_z\phi=0`$, и $`\partial_{\bar z}T_{zz}=2g(\nabla_{\partial_{\bar z}}\partial_z\phi,\partial_z\phi)=0`$. Критерии: 2 + 2 + 2.

**C2.** (а) Если $`V(\phi(+\infty))>0`$, то $`\int V=\infty`$; значит, $`\phi(\pm\infty)\in\lbrace\pm v\rbrace`$. С $`W'=\sqrt{\lambda/2}(v^2-\phi^2)`$, $`\frac12W'^2=V`$:

<div align="center">

$`\displaystyle E[\phi]=\frac12\int\left(\phi'\mp W'(\phi)\right)^2dx\pm\left(W(\phi(+\infty))-W(\phi(-\infty))\right),`$

</div>

равенство при $`\phi'=\pm W'(\phi)`$ (уравнение Богомольного). (б) Первый интеграл $`\frac12\phi'^2=V(\phi)`$ (константа $`0`$ из конечности энергии, как в B5), $`-v<\phi<v`$ по единственности, $`\phi'=\sqrt{\lambda/2}(v^2-\phi^2)`$: $`\phi_K=v\tanh\left(\kappa(x-x_0)\right)`$, $`\kappa=v\sqrt{\lambda/2}`$. $`M=W(v)-W(-v)=\frac{2\sqrt2}{3}\sqrt\lambda v^3`$. (в) Дифференцируя $`\phi_K''=V'(\phi_K)`$: $`\mathcal{L}\phi_K'=0`$ — производная семейства сдвигов по $`x_0`$ (трансляционная мода). $`\phi_K'=v\kappa\,\mathrm{sech}^2(\kappa x)>0`$, $`\in L^2`$; собственная функция без нулей отвечает низу спектра (Штурм), значит, $`\mathcal{L}\ge0`$. Явно $`\mathcal{L}=-\frac{d^2}{dx^2}+4\kappa^2-6\kappa^2\mathrm{sech}^2(\kappa x)`$, дискретный спектр $`\lbrace0,3\kappa^2\rbrace`$, непрерывный $`[4\kappa^2,\infty)`$. Критерии: 2 + 2 + 2.

**C3.** (а) $`f=0`$, голономия $`e^{i\Phi}`$. Голономия калибровочно инвариантна, у $`a=0`$ она равна $`1`$; при $`\Phi=2\pi n`$ преобразование $`e^{i\lambda}=e^{-in\theta}`$ переводит $`a`$ в $`0`$. (б) $`df=0`$ (коэффициент не зависит от $`r`$); $`\int_{S^2}f=2\pi m`$; если $`f=da`$, то по Стоксу $`\int_{S^2}f=0`$. (в) $`a_N=\frac m2(1-\cos\theta)d\varphi=\frac m2\frac{x^1dx^2-x^2dx^1}{r(r+x^3)}`$, $`a_S=-\frac m2(1+\cos\theta)d\varphi=-\frac m2\frac{x^1dx^2-x^2dx^1}{r(r-x^3)}`$ — гладкие где нужно. $`a_N-a_S=m\,d\varphi`$; пересечение гомотопно окружности, и $`a_N=a_S+d\lambda`$ с однозначной $`e^{i\lambda}=e^{im\varphi}`$ возможно ровно при $`m\in\mathbb{Z}`$ (квантование Дирака). $`c_1=\frac{1}{2\pi}\int_{S^2}f=m`$. Критерии: 2 + 2 + 2.

**C4.** (а) $`\delta\,\mathrm{tr}(A\wedge dA)=2\,\mathrm{tr}(b\wedge dA)-d\,\mathrm{tr}(A\wedge b)`$, $`\delta\frac23\mathrm{tr}(A^3)=2\,\mathrm{tr}(b\wedge A^2)`$ (цикличность со знаками); интегрируя, получаем формулу. Критические точки — плоские связности. (б) Пусть $`\mathrm{cs}_3(A)=\mathrm{tr}\left(A\wedge F_A-\frac13A^3\right)`$ — подынтегральная форма, $`\Theta=dg\,g^{-1}`$, $`d\Theta=\Theta^2`$, $`A^g=g^{-1}(A+\Theta)g`$, $`F_{A^g}=g^{-1}F_Ag`$. Тогда

<div align="center">

$`\displaystyle \mathrm{cs}_3(A^g)=\mathrm{tr}\left((A+\Theta)F_A\right)-\frac13\mathrm{tr}\left((A+\Theta)^3\right)=\mathrm{cs}_3(A)+\mathrm{tr}(\Theta\wedge dA)-\mathrm{tr}(A\wedge\Theta^2)-\frac13\mathrm{tr}(\Theta^3),`$

</div>

и так как $`d\,\mathrm{tr}(\Theta\wedge A)=\mathrm{tr}(A\wedge\Theta^2)-\mathrm{tr}(\Theta\wedge dA)`$, получаем $`\mathrm{cs}_3(A^g)=\mathrm{cs}_3(A)-\frac13\mathrm{tr}\left((g^{-1}dg)^3\right)-d\,\mathrm{tr}(dg\,g^{-1}\wedge A)`$; интегрируем по $`Y`$. (в) $`e^{2\pi i\ell\,\mathrm{cs}}`$ умножается на $`e^{-2\pi i\ell w(g)}=1`$. Для гомотопии $`g_t`$ функция $`w(g_t)`$ непрерывна и целочисленна, $`w(\mathrm{const})=0`$. Критерии: 2 + 3 + 1.

**C5.** (а) $`\partial_\mu f^{\mu\nu}=j^\nu`$ ($`df=0`$ — тождество). (б) $`T_{\mathrm{can}}^{\mu\nu}=-f^{\mu\lambda}\partial^\nu a_\lambda+\frac14\eta^{\mu\nu}f_{\alpha\beta}f^{\alpha\beta}`$; при $`a\mapsto a+d\lambda`$ появляется $`-f^{\mu\lambda}\partial^\nu\partial_\lambda\lambda`$, антисимметричная часть, вообще говоря, ненулевая. Для любых $`a`$: $`T_{\mathrm{can}}^{\mu\nu}=T^{\mu\nu}+\partial_\lambda(f^{\lambda\mu}a^\nu)-(\partial_\lambda f^{\lambda\mu})a^\nu`$ (так как $`f^\nu{}_\lambda=\partial^\nu a_\lambda-\partial_\lambda a^\nu`$), последний член $`0`$ при $`j=0`$. Добавка антисимметрична по $`\lambda\mu`$: её дивергенция по $`\mu`$ равна $`0`$, а вклад в $`P^\nu`$ — поверхностный интеграл $`\int\partial_iB^{i0\nu}`$, исчезающий при $`\lvert f\rvert\lvert a\rvert=o(\lvert x\rvert^{-2})`$. (в) $`T^{00}=\frac12(\lvert E\rvert^2+\lvert B\rvert^2)`$, $`T^{0i}=(E\times B)_i`$, $`T^\mu{}_\mu=0`$ (вейлевская инвариантность в размерности $`4`$; в размерности $`n`$ след $`(\frac n4-1)f_{\alpha\beta}f^{\alpha\beta}`$). $`\partial_\mu T^{\mu\nu}=-f^{\nu\lambda}j_\lambda`$; при $`\nu=0`$: $`\partial_tT^{00}+\mathrm{div}(E\times B)=-E\cdot J`$ — теорема Пойнтинга. Критерии: (а) — 1; (б) — 3; (в) — 2.

### Часть D

**D1.** Схема.
1. (а) $`F_{A+tb}=F_A+t(db+A\wedge b+b\wedge A)+t^2b\wedge b`$, $`db+[A\wedge b]=D_Ab`$. Так как $`d\,\mathrm{tr}(b\wedge\ast F)=\mathrm{tr}(D_Ab\wedge\ast F)-\mathrm{tr}(b\wedge D_A\ast F)`$ и $`M`$ замкнуто,

<div align="center">

$`\displaystyle \frac{d}{dt}\Big\rvert_{0}S_{YM}(A+tb)=-2\int_M\mathrm{tr}(D_Ab\wedge\ast F_A)=-2\int_M\mathrm{tr}(b\wedge D_A\ast F_A).`$

</div>

При $`b=\ast D_A\ast F_A`$ это $`\pm2\lVert D_A\ast F_A\rVert^2_{L^2}`$, так что критичность $`\iff D_A\ast F_A=0`$. На $`\mathbb{R}^4`$: $`\partial_\mu F_{\mu\nu}+[A_\mu,F_{\mu\nu}]=0`$.
2. (б) $`dF=dA\wedge A-A\wedge dA`$, $`[A\wedge F]=A\wedge dA-dA\wedge A`$ (кубические члены сокращаются).
3. (в) $`F=F^++F^-`$; $`\mathrm{tr}(F^+\wedge F^-)=-\mathrm{tr}(F^+\wedge\ast F^-)=\langle F^+,F^-\rangle d\mathrm{vol}=0`$, $`-\mathrm{tr}(F^\pm\wedge F^\pm)=\pm\lvert F^\pm\rvert^2d\mathrm{vol}`$. Поэтому

<div align="center">

$`\displaystyle S_{YM}=\int\left(\lvert F^+\rvert^2+\lvert F^-\rvert^2\right),\qquad8\pi^2k=\int\left(\lvert F^+\rvert^2-\lvert F^-\rvert^2\right),`$

</div>

$`S_{YM}\mp8\pi^2k=2\int\lvert F^\mp\rvert^2\ge0`$, откуда $`S_{YM}\ge8\pi^2\lvert k\rvert`$; при $`k\ge0`$ равенство $`\iff F^-=0`$, при $`k\le0`$ — $`\iff F^+=0`$.
4. (г) $`F=\pm\ast F\Rightarrow D_A\ast F=\pm D_AF=0`$; нижняя грань $`8\pi^2\lvert k(P)\rvert`$ общая для всех связностей на $`P`$. Для автодуальной $`8\pi^2k=\int\lvert F\rvert^2>0`$ (то есть $`c_2(P)<0`$).

Критерии: (а) — 4 (формула для $`F_{A+tb}`$ — 1, вариация с интегрированием по частям — 2, вывод уравнения — 1); (б) — 1; (в) — 4 (формулы для $`S`$ и $`k`$ — 2, неравенство и равенство — 2); (г) — 1. Для засчитывания КТ нужны (а) и (в) полностью.

**D2.** Схема.
1. (а) Пусть $`u=(\rho^2+\lvert x\rvert^2)^{-1}`$, $`\alpha=\mathrm{Im}(x\,d\bar x)`$; $`d\alpha=dx\wedge d\bar x`$, поэтому $`F_A=u\,dx\wedge d\bar x+du\wedge\alpha+u^2\alpha\wedge\alpha`$. При $`L(x)=px\bar q`$: $`L^{\ast}(x\,d\bar x)=p\,x\,d\bar x\,\bar p`$, $`L^{\ast}A=pA\bar p`$ (калибровка постоянной $`\bar p`$), $`L^{\ast}F_A=pF_A\bar p`$, и правая часть преобразуется так же; любая точка — $`L(t)`$ с $`t=\lvert x\rvert`$, $`p=x/\lvert x\rvert`$, $`q=1`$. В точке $`x=t`$, с $`dv=i\,dx^1+j\,dx^2+k\,dx^3`$: $`\alpha=-t\,dv`$, $`du=-2tu^2dx^0`$, $`du\wedge\alpha+u^2\alpha\wedge\alpha=t^2u^2(2dx^0\wedge dv+dv\wedge dv)=-t^2u^2dx\wedge d\bar x`$, так как $`dx\wedge d\bar x=-2dx^0\wedge dv-dv\wedge dv`$. Итого $`F_A=u(1-t^2u)dx\wedge d\bar x=\rho^2u^2dx\wedge d\bar x`$.
2. (б) $`dv\wedge dv=2(i\,dx^2\wedge dx^3+j\,dx^3\wedge dx^1+k\,dx^1\wedge dx^2)`$ (например, $`ij-ji=2k`$), поэтому

<div align="center">

$`\displaystyle dx\wedge d\bar x=-2\left[i\left(dx^{01}+dx^{23}\right)+j\left(dx^{02}+dx^{31}\right)+k\left(dx^{03}+dx^{12}\right)\right],\qquad dx^{\mu\nu}=dx^\mu\wedge dx^\nu .`$

</div>

Перестановки $`0123`$, $`0231`$, $`0312`$ чётны, так что $`\ast dx^{01}=dx^{23}`$, $`\ast dx^{02}=dx^{31}`$, $`\ast dx^{03}=dx^{12}`$, и каждая скобка автодуальна. (Для сравнения: $`\mathrm{Im}(\bar x\,dx)/(\rho^2+\lvert x\rvert^2)`$ даёт антиавтодуальный инстантон с $`k=-1`$.)
3. (в) Для $`X=cu_0`$, $`u_0`$ — единичный мнимый кватернион, $`-\mathrm{tr}(X^2)=2c^2`$; у $`dx\wedge d\bar x`$ шесть компонент вида $`-2u_0`$, $`\lvert dx\wedge d\bar x\rvert^2=48`$, $`\lvert F_A\rvert^2=48\rho^4u^4=O(\lvert x\rvert^{-8})`$:

<div align="center">

$`\displaystyle S_{YM}(A)=48\rho^4\cdot2\pi^2\int_0^\infty\frac{r^3dr}{(\rho^2+r^2)^4}=96\pi^2\rho^4\cdot\frac{1}{12\rho^4}=8\pi^2 .`$

</div>

Так как $`F_A=\ast F_A`$, $`-\mathrm{tr}(F_A\wedge F_A)=\lvert F_A\rvert^2d\mathrm{vol}`$ и $`k=S_{YM}/8\pi^2=1`$. Растяжение $`x\mapsto\rho x`$ переводит инстантон масштаба $`1`$ в инстантон масштаба $`\rho`$, а $`S_{YM}`$ и $`k`$ конформно инвариантны.

Критерии: (а) — 4 (общий вид $`F`$ — 1, сведение к $`x=t`$ — 1, вычисление — 2; прямое вычисление без симметрии засчитывается полностью); (б) — 3; (в) — 3. Для засчитывания КТ нужны все три пункта.

### Часть E

**E1.** (а) Из $`\bar\phi D\phi=\bar\phi\,d\phi-ia\lvert\phi\rvert^2`$: $`a=d\arg\phi-\mathrm{Im}(\bar\phi D\phi)/\lvert\phi\rvert^2`$ при больших $`\lvert x\rvert`$. По Стоксу $`\int_{B_R}f_{12}=\oint_{C_R}a=2\pi N+o(1)`$, так как $`\oint_{C_R}\lvert D\phi\rvert/\lvert\phi\rvert\le2\pi R\sup_{C_R}\lvert D\phi\rvert/\lvert\phi\rvert\to0`$; $`f_{12}\in L^1`$ даёт предел. (б) Тождество: $`\lvert D_1\phi+iD_2\phi\rvert^2=\lvert D_1\phi\rvert^2+\lvert D_2\phi\rvert^2+2\,\mathrm{Im}(D_1\phi\overline{D_2\phi})`$ и $`\partial_1J_2-\partial_2J_1=-2\,\mathrm{Im}(D_1\phi\overline{D_2\phi})-f_{12}\lvert\phi\rvert^2`$ (через $`[D_1,D_2]=-if_{12}`$). С $`f_{12}^2+\frac14(1-\lvert\phi\rvert^2)^2=\left(f_{12}-\frac12(1-\lvert\phi\rvert^2)\right)^2+f_{12}(1-\lvert\phi\rvert^2)`$:

<div align="center">

$`\displaystyle E=\frac12\int\left[\left(f_{12}-\tfrac12(1-\lvert\phi\rvert^2)\right)^2+\lvert D_1\phi+iD_2\phi\rvert^2\right]+\pi N+\frac12\lim_{R\to\infty}\oint_{C_R}J,`$

</div>

а $`\lvert J\rvert\le\lvert\phi\rvert\lvert D\phi\rvert=o(1/R)`$. Значит, $`E\ge\pi N`$ с равенством ровно при уравнениях Богомольного; с $`D_1\phi-iD_2\phi`$ аналогично $`E\ge-\pi N`$. (в) $`\int f_{12}^2`$ умножается на $`\lambda^2`$, $`\int\lvert D\phi\rvert^2`$ не меняется, $`\int(1-\lvert\phi\rvert^2)^2`$ умножается на $`\lambda^{-2}`$: член калибровочного поля растёт при растяжении, и аргумент Деррика не проходит. $`\frac{d}{d\lambda}E\big\rvert_{\lambda=1}=0`$ даёт тождество; для решений Богомольного оно верно поточечно. Критерии: (а) — 3; (б) — 3; (в) — 1.

**E2.** (а) $`\mathrm{tr}(F\wedge F)=\mathrm{tr}(dA\wedge dA)+2\,\mathrm{tr}(dA\wedge A^2)+\mathrm{tr}(A^4)`$, $`\mathrm{tr}(A^4)=0`$; $`d\,\mathrm{tr}(A\wedge dA)=\mathrm{tr}(dA\wedge dA)`$, $`d\,\mathrm{tr}(A^3)=3\,\mathrm{tr}(dA\wedge A^2)`$. (б) $`F=0`$ вне $`B_{R_0}`$, по Стоксу $`k=-\frac{1}{8\pi^2}\int_{S^3_R}\mathrm{cs}_3(A)`$; при $`A=\theta=g^{-1}dg`$, $`d\theta=-\theta^2`$: $`\mathrm{cs}_3(\theta)=-\frac13\mathrm{tr}(\theta^3)`$, и $`k=w(g)`$. (в) $`X=h^{-1}\dot h`$: $`\dot\theta=dX+[\theta,X]`$, $`\mathrm{tr}([\theta,X]\theta^2)=0`$, $`d(\theta^2)=0`$, поэтому $`\frac{d}{ds}\mathrm{tr}(\theta^3)=3\,\mathrm{tr}(\dot\theta\theta^2)=3\,d\,\mathrm{tr}(X\theta^2)`$, и интеграл по $`S^3`$ постоянен. (г) $`\mathrm{tr}(\theta^3)`$ — прообраз биинвариантной формы при изометрии $`g\rvert_{S^3}`$, её плотность постоянна; в точке $`x=1`$: $`dg=d\bar x-dx^0=-dv`$, $`\theta^3=-(dv)^3=6\,dx^1\wedge dx^2\wedge dx^3`$ ($`ijk=-1`$), $`\mathrm{tr}(\theta^3)=12\,dx^{123}`$, а $`(\partial_1,\partial_2,\partial_3)`$ положителен для ориентации границы. $`w(g)=\frac{12\cdot2\pi^2}{24\pi^2}=1`$. Для BPST $`A-g^{-1}dg=-\frac{\rho^2\,\mathrm{Im}(x\,d\bar x)}{\lvert x\rvert^2(\rho^2+\lvert x\rvert^2)}=O(\lvert x\rvert^{-3})`$, поэтому $`\mathrm{cs}_3(A)-\mathrm{cs}_3(g^{-1}dg)=O(R^{-5})`$ на $`S^3_R`$, и $`k=-\lim\frac{1}{8\pi^2}\int_{S^3_R}\mathrm{cs}_3(A)=w(g)=1`$ — в согласии с D2. Критерии: 2 + 2 + 2 + 2.

</details>
