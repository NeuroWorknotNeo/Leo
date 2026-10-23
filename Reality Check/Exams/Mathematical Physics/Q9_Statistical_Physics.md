# Q9. Статистическая физика — диагностика

> **Код в плане:** [Q9](../../PLAN.md#q9) · **Время:** ≈ 230 минут ([расширенный экзамен](../../README.md#physics)) · **Максимум:** 100 баллов · **Этап плана:** 4 (боковая ветвь)
>
> **Требует:** Q1, P1, R2; Q2 для квантовой части. **Можно пользоваться:** только бумагой и ручкой (никаких книг, конспектов, интернета, CAS).

## Как проходить

1. Засечь 230 минут или сдавать в два захода: части A–C (125 минут), затем D–E (105 минут); подробнее — в [особых правилах для физики](../../README.md#physics). Ориентировочное время на части указано в заголовках; переходить к следующей части можно в любой момент.
2. Писать решения полностью, как на письменном экзамене. «Понятно, как делать» без записи — 0 баллов.
3. Ключ в конце файла открывать только после окончания времени. Проверять себя строго, по критериям из ключа.
4. Записать баллы по частям в таблицу результатов в конце и прочитать интерпретацию.

Соглашения: $`k_B=1`$, $`\beta=1/T>0`$ (в C1 — любого знака). Фазовое пространство $`N`$ частиц несёт меру $`d^{dN}q\,d^{dN}p/\left((2\pi)^{dN}N!\right)`$ (то есть $`\hbar=1`$), $`\lambda=\sqrt{2\pi\beta/m}`$ — тепловая длина волны. Модель Изинга: $`\Omega=\lbrace-1,1\rbrace^{\mathbb{Z}^d}`$ (топология и $`\sigma`$-алгебра произведения), $`i\sim j`$ — соседи, $`\Lambda\subset\mathbb{Z}^d`$ конечно, $`\Lambda_n=\lbrace-n,\dots,n\rbrace^d`$, $`J>0`$. Для $`\eta\in\Omega`$: $`\Omega^\eta_\Lambda=\lbrace\sigma:\sigma_i=\eta_i\ \forall i\notin\Lambda\rbrace`$, $`H^\eta_\Lambda(\sigma)=-J\sum_{\lbrace i,j\rbrace\in\mathcal{E}^b_\Lambda}\sigma_i\sigma_j-h\sum_{i\in\Lambda}\sigma_i`$, где $`\mathcal{E}^b_\Lambda`$ — пары соседей, задевающие $`\Lambda`$; $`\mu^\eta_{\Lambda;\beta,h}=e^{-\beta H^\eta_\Lambda}/Z^\eta_{\Lambda;\beta,h}`$ на $`\Omega^\eta_\Lambda`$, средние $`\langle\cdot\rangle^\eta_{\Lambda;\beta,h}`$. Граничные условия «$`\pm`$» — $`\eta\equiv\pm1`$; свободное ($`\varnothing`$) — в $`H`$ только пары внутри $`\Lambda`$. Давление $`\psi(\beta,h)=\lim_n\lvert\Lambda_n\rvert^{-1}\log Z_{\Lambda_n;\beta,h}`$. $`\mu^\pm_{\beta,h}`$ — слабые пределы $`\mu^\pm_{\Lambda_n;\beta,h}`$, $`\langle\cdot\rangle^\pm_{\beta,h}`$ — средние по ним; $`m^{\ast}(\beta)=\langle\sigma_0\rangle^+_{\beta,0}`$, $`\beta_c(d)=\inf\lbrace\beta:m^{\ast}(\beta)>0\rbrace`$; $`\mathcal{G}(\beta,h)`$ — множество мер Гиббса (A4).

## Часть A. Определения и формулировки (≈ 30 мин, 20 баллов)

Дать точные определения / сформулировать теоремы полностью, со всеми условиями. 10 пунктов по 2 балла.

1. Канонический и большой канонический ансамбли классического газа в ограниченной $`\Lambda\subset\mathbb{R}^d`$, $`H_N=\sum_i\lvert p_i\rvert^2/(2m)+U_N(q)`$: статсуммы $`Z_N`$, $`\Xi`$ и вероятностные меры (на каких пространствах). Какое условие на гамильтониан квантовой системы нужно для состояния Гиббса? Выразить среднюю энергию и её дисперсию через $`\log Z_N`$.
2. Микроканонический ансамбль (для конечного множества конфигураций и для классической системы с гладким $`H`$), энтропия Больцмана. Удельная микроканоническая энтропия $`s(e)`$ модели Изинга при $`h=0`$ и её связь с $`\psi(\beta,0)`$ (эквивалентность ансамблей): формулы и свойства $`s`$.
3. Сходимость $`\Lambda_n\uparrow\mathbb{Z}^d`$ по Ван Хову. Теорема о существовании давления модели Изинга: от чего предел не зависит, какие свойства у $`\psi`$.
4. Спецификация модели Изинга, условие DLR, определение $`\mathcal{G}(\beta,h)`$. Структура $`\mathcal{G}(\beta,h)`$: непустота, выпуклость, компактность, крайние точки.
5. Фазовый переход как неединственность меры Гиббса. Для модели Изинга: связь $`\langle\sigma_0\rangle^\pm_{\beta,h}`$ с односторонними производными $`\psi`$ по $`h`$, критерий единственности, фазовая диаграмма в плоскости $`(\beta,h)`$ при $`d\ge2`$ и при $`d=1`$ (точку $`(\beta_c,0)`$ не рассматривать).
6. Неравенства Гриффитса GKS-1, GKS-2 и неравенство FKG: для каких мер и функций, условия на знаки констант связи и полей.
7. Решение Онсагера (формулировка): $`\beta_c(2)`$, спонтанная намагниченность $`m^{\ast}(\beta)`$ (формула Онсагера–Янга), аналитичность $`\psi(\beta,0)`$ по $`\beta`$.
8. Теорема Ли–Янга о кольце: класс моделей, в каком смысле $`Z_\Lambda`$ — многочлен, утверждение, следствие для давления.
9. Критические показатели $`\hat\beta,\hat\gamma,\hat\delta,\nu`$ (крышка — чтобы не путать с $`\beta=1/T`$): определения; значения в теории среднего поля и при $`d=2`$.
10. Ренормгруппа (обзор): блок-спиновое преобразование $`R_b`$, неподвижная точка, релевантные и иррелевантные направления; выражение $`\nu`$ через линеаризацию $`R_b`$; универсальность.

## Часть B. Верно или неверно? (≈ 25 мин, 15 баллов)

Для каждого утверждения ответить «верно» или «неверно» и **обосновать**: короткое доказательство или контрпример. Ответ без обоснования — 0 баллов. 5 пунктов по 3 балла.

1. Пусть $`d=2`$. Если $`\beta\mapsto\psi(\beta,0)`$ дифференцируема в точке $`\beta_0`$, то $`\mathcal{G}(\beta_0,0)`$ состоит из одной меры.
2. В модели Кюри–Вейсса (обозначения C3) при $`h=0`$, $`\beta J>1`$ распределение $`m_N`$ относительно $`\mu_N`$ слабо сходится к $`\frac12(\delta_{m^{\ast}}+\delta_{-m^{\ast}})`$, где $`m^{\ast}>0`$ — корень $`m=\tanh(\beta Jm)`$.
3. Для модели Изинга на $`\mathbb{Z}^d`$ со свободным граничным условием и $`h=0`$ корреляция $`\langle\sigma_0\sigma_x\rangle^\varnothing_{\Lambda;\beta,0}`$ не убывает по $`\beta`$ и по $`\Lambda`$ (при $`0,x\in\Lambda\subset\Lambda'`$).
4. Для двумерной модели Изинга ($`h=0`$, свободное граничное условие) и любой возрастающей последовательности конечных $`\Lambda_n`$ с $`\bigcup_n\Lambda_n=\mathbb{Z}^2`$ предел $`\lvert\Lambda_n\rvert^{-1}\log Z^\varnothing_{\Lambda_n;\beta,0}`$ существует и равен $`\psi(\beta,0)`$.
5. Теорема Ли–Янга верна и для антиферромагнетиков: если все $`J_{ij}\le0`$, то нули $`Z_\Lambda`$ как многочлена от $`z=e^{-2\beta h}`$ лежат на $`\lvert z\rvert=1`$.

## Часть C. Стандартные задачи (≈ 70 мин, 30 баллов)

Вычисления и рутинные доказательства, которые должен уверенно делать каждый, кто прошёл курс. 5 задач по 6 баллов.

**C1.** Вариационный принцип Гиббса. $`\Omega`$ конечно, $`H\colon\Omega\to\mathbb{R}`$ непостоянна, $`\mu_\beta=e^{-\beta H}/Z(\beta)`$, $`\beta\in\mathbb{R}`$, $`S(\mu)=-\sum_\omega\mu(\omega)\log\mu(\omega)`$. (а) Доказать, что $`S(\mu)-\beta\langle H\rangle_\mu\le\log Z(\beta)`$ для любой вероятностной меры $`\mu`$ на $`\Omega`$, с равенством только при $`\mu=\mu_\beta`$. (б) Доказать: для каждого $`E\in(\min H,\max H)`$ есть единственное $`\beta(E)`$ с $`\langle H\rangle_{\mu_{\beta(E)}}=E`$; максимум $`S(\mu)`$ при $`\langle H\rangle_\mu=E`$ достигается только на $`\mu_{\beta(E)}`$; $`S_{\max}'(E)=\beta(E)`$. Когда $`\beta(E) < 0`$? (в) $`\Omega=\lbrace0,1\rbrace^N`$, $`H(x)=\varepsilon\sum_ix_i`$, $`\varepsilon>0`$: найти $`\beta(E)`$ и $`S_{\max}(E)/N`$ как функции $`e=E/N\in(0,\varepsilon)`$ и сравнить с $`\frac1N\log\#\lbrace H=E\rbrace`$ при $`N\to\infty`$, $`E/N\to e`$.

**C2.** Идеальный газ и равнораспределение. $`N`$ частиц массы $`m`$ в кубе $`\Lambda\subset\mathbb{R}^3`$ объёма $`V`$, $`H_N=\sum_i\lvert p_i\rvert^2/(2m)`$. (а) Доказать, что $`Z_N=(V/\lambda^3)^N/N!`$; найти $`f=-\lim\frac{1}{\beta N}\log Z_N`$ при $`N,V\to\infty`$, $`N/V=\rho`$, давление $`P=\beta^{-1}\partial_V\log Z_N`$ и среднюю энергию. (б) Найти $`s=\lim S/N`$, $`S=\log Z_N+\beta\langle H_N\rangle`$ (Сакура–Тетроде). Что будет без $`1/N!`$? (в) Пусть $`H\in C^1(\mathbb{R}^n)`$, $`e^{-\beta H}`$ и $`x_i\,\partial_jH\,e^{-\beta H}`$ интегрируемы, $`x_ie^{-\beta H}\to0`$ при $`\lvert x_j\rvert\to\infty`$. Доказать, что $`\langle x_i\,\partial_jH\rangle=\delta_{ij}T`$. Вывести, что кинетическая энергия частицы газа в среднем равна $`\frac32T`$, а для гармонического кристалла $`H=\sum_{i=1}^N\lvert p_i\rvert^2/(2m)+\frac12\langle q,Kq\rangle`$ на $`\mathbb{R}^{6N}`$, $`K>0`$, имеем $`\langle H\rangle=3NT`$.

**C3.** Модель Кюри–Вейсса. На $`\lbrace-1,1\rbrace^N`$: $`H_N=-\frac{J}{2N}\left(\sum_i\sigma_i\right)^2-h\sum_i\sigma_i`$, $`J>0`$, $`\mu_N\propto e^{-\beta H_N}`$, $`m_N=\frac1N\sum_i\sigma_i`$, $`I(m)=\frac{1+m}{2}\log(1+m)+\frac{1-m}{2}\log(1-m)`$. (а) Доказать, что

```math
\psi(\beta,h):=\lim_{N\to\infty}\frac1N\log Z_N=\log2+\max_{m\in[-1,1]}\varphi(m),\qquad \varphi(m)=\beta\left(\frac J2m^2+hm\right)-I(m)
```

(можно использовать: $`\frac1N\log\binom Nk=\log2-I(1-2k/N)+O(\frac{\log N}N)`$ равномерно по $`k`$). (б) Доказать, что точки максимума $`\varphi`$ удовлетворяют $`m=\tanh(\beta(Jm+h))`$, а при $`h=0`$ максимум единственен ($`m=0`$) при $`\beta J\le1`$ и достигается ровно в $`\pm m^{\ast}(\beta)`$, $`m^{\ast}>0`$, при $`\beta J>1`$. (в) Найти асимптотику $`m^{\ast}(\beta)`$ при $`\beta\downarrow1/J`$ и точки максимума $`m(h)`$ при $`\beta=1/J`$, $`h\downarrow0`$. Чему равны $`\hat\beta`$ и $`\hat\delta`$?

**C4.** Квантовые идеальные газы ($`\hbar=1`$). Одночастичный $`-\Delta/(2m)`$ на торе $`(\mathbb{R}/L\mathbb{Z})^d`$ имеет спектр $`\varepsilon_k=\lvert k\rvert^2/(2m)`$, $`k\in\frac{2\pi}{L}\mathbb{Z}^d`$; $`\Xi=\mathrm{tr}\,e^{-\beta(H-\mu N)}`$ на бозонном или фермионном пространстве Фока. (а) Доказать, что $`\Xi=\prod_k(1\mp e^{-\beta(\varepsilon_k-\mu)})^{\mp1}`$ (при каких $`\mu`$?), и вывести распределения Бозе–Эйнштейна и Ферми–Дирака для $`\langle n_k\rangle`$. (б) Для бозонов при $`\mu < 0`$ доказать, что $`\rho_d(\beta,\mu):=\lim_{L\to\infty}L^{-d}\sum_k\langle n_k\rangle=\lambda^{-d}g_{d/2}(e^{\beta\mu})`$, $`g_s(z)=\sum_{j\ge1}z^j/j^s`$ (можно не доказывать, что $`L^{-d}\sum_kF(k)\to(2\pi)^{-d}\int F`$ для непрерывной интегрируемой радиально убывающей $`F\ge0`$). (в) Найти $`\sup_{\mu < 0}\rho_d`$ при $`d=3`$ и $`d=2`$. Объяснить (на физическом уровне строгости), что происходит при $`\rho>\rho_c(\beta)`$ в $`d=3`$, найти $`T_c(\rho)`$. Есть ли конденсация при $`d=2`$?

**C5.** Термодинамический предел. Модель Изинга на $`\mathbb{Z}^d`$, свободное граничное условие, $`Z_\Lambda:=Z^\varnothing_{\Lambda;\beta,h}`$, $`C_\ell=\lbrace1,\dots,\ell\rbrace^d`$. (а) Доказать, что для непересекающихся $`\Lambda_1,\Lambda_2`$ выполнено $`\lvert\log Z_{\Lambda_1\cup\Lambda_2}-\log Z_{\Lambda_1}-\log Z_{\Lambda_2}\rvert\le\beta J\,e(\Lambda_1,\Lambda_2)`$ ($`e`$ — число пар соседей между ними) и $`\lvert\log Z_\Lambda\rvert\le\lvert\Lambda\rvert(\log2+\beta Jd+\beta\lvert h\rvert)`$. (б) Для $`a_k=2^{-kd}\log Z_{C_{2^k}}`$ доказать $`\lvert a_{k+1}-a_k\rvert\le\beta Jd\,2^{-k-1}`$; значит, $`a_k`$ сходится. (в) Доказать, что $`n^{-d}\log Z_{C_n}\to\lim_ka_k`$ по всем $`n\to\infty`$. (г) Доказать, что с граничным условием «$`+`$» предел тот же.

## Часть D. Ключевые доказательства (≈ 60 мин, 20 баллов)

Доказать центральные теоремы курса. Сюда входит контрольная точка из plan.md. 2 задачи по 10 баллов.

**D1.** *(контрольная точка)* Одномерная модель Изинга на кольце $`\mathbb{Z}/N\mathbb{Z}`$: $`H_N=-J\sum_{i=1}^N\sigma_i\sigma_{i+1}-h\sum_{i=1}^N\sigma_i`$ (индексы по модулю $`N`$), $`J>0`$, $`h\in\mathbb{R}`$, $`\mu_N\propto e^{-\beta H_N}`$, средние $`\langle\cdot\rangle_N`$.

(а) Доказать, что $`Z_N=\mathrm{tr}\,T^N`$, где

```math
T=\begin{pmatrix}e^{\beta(J+h)}&e^{-\beta J}\\ e^{-\beta J}&e^{\beta(J-h)}\end{pmatrix},
```

и найти собственные значения $`\lambda_+>\lambda_->0`$.

(б) Найти $`\psi(\beta,h)=\lim\frac1N\log Z_N`$, доказать её вещественную аналитичность по $`h\in\mathbb{R}`$ и то, что со свободным граничным условием на $`\lbrace1,\dots,N\rbrace`$ предел тот же.

(в) Найти $`m(\beta,h)=\lim_N\langle\sigma_1\rangle_N`$, проверить $`m=\beta^{-1}\partial_h\psi`$, найти $`\lim_{h\downarrow0}m(\beta,h)`$.

(г) Доказать, что $`\lim_N\left(\langle\sigma_0\sigma_r\rangle_N-\langle\sigma_0\rangle_N\langle\sigma_r\rangle_N\right)=A\,e^{-r/\xi}`$; найти $`A`$ и $`\xi(\beta,h)`$, явно — $`\langle\sigma_0\sigma_r\rangle`$ и $`\xi`$ при $`h=0`$ и асимптотику $`\xi`$ при $`\beta\to\infty`$.

(д) При $`h=0`$ на $`\lbrace-n,\dots,n\rbrace`$ с граничным условием «$`+`$» (спины в $`\pm(n+1)`$ равны $`+1`$) вычислить $`\langle\sigma_0\rangle^+_n`$ и его предел. Объяснить, почему при $`T>0`$ нет фазового перехода ни как неаналитичности $`\psi`$, ни как неединственности меры Гиббса (можно использовать: если $`\langle\sigma_0\rangle^+_{\beta,h}=\langle\sigma_0\rangle^-_{\beta,h}`$, то $`\lvert\mathcal{G}(\beta,h)\rvert=1`$).

**D2.** *(контрольная точка)* Аргумент Пайерлса. $`d=2`$, $`h=0`$, $`\mu^+_n:=\mu^+_{\Lambda_n;\beta,0}`$ на $`\Omega^+_{\Lambda_n}`$ (см. соглашения).

(а) Определить контуры конфигурации $`\omega\in\Omega^+_{\Lambda_n}`$ (через рёбра двойственной решётки $`\mathbb{Z}^2+(\frac12,\frac12)`$, с правилом расщепления в вершинах степени $`4`$) и доказать, что $`H^+_{\Lambda_n}(\omega)=H^+_{\Lambda_n}(+)+2J\sum_\gamma\lvert\gamma\rvert`$ (сумма по контурам $`\omega`$, $`\lvert\gamma\rvert`$ — длина). Доказать, что при $`\omega_0=-1`$ некоторый контур окружает $`0`$.

(б) Доказать неравенство Пайерлса: $`\mu^+_n(\gamma\ \text{— контур}\ \omega)\le e^{-2\beta J\lvert\gamma\rvert}`$ для каждого фиксированного $`\gamma`$.

(в) Доказать, что контуров длины $`\ell`$, окружающих $`0`$, не больше $`\frac\ell2\cdot3^{\ell-1}`$, и получить явную оценку $`\mu^+_n(\sigma_0=-1)\le\varepsilon(\beta)`$, равномерную по $`n`$. Проверить, что при $`\beta J\ge1`$ имеем $`\langle\sigma_0\rangle^+_{\Lambda_n;\beta,0}\ge0{,}9`$ при всех $`n`$.

(г) Построить предельную меру $`\mu^+_\beta`$ как предельную точку $`\mu^+_n`$ (продолженных на $`\Omega`$), доказать, что $`\mu^+_\beta\in\mathcal{G}(\beta,0)`$, и вывести, что при $`\beta J\ge1`$ мера Гиббса не единственна и $`\beta_c(2)\le1/J`$.

## Часть E. Задачи повышенной сложности (≈ 45 мин, 15 баллов)

Нестандартные задачи: проверяют, умеете ли вы применять теорию там, где путь не подсказан. Не огорчайтесь, если не все решены. E1 — 7 баллов, E2 — 8 баллов.

**E1.** Двойственность Крамерса–Ванье. $`G=(V,E)`$ — конечный связный простой плоский граф, $`G^{\ast}`$ — двойственный мультиграф (вершины — грани $`G`$, включая внешнюю). Для мультиграфа $`\Gamma`$ пусть $`Z_\Gamma(\beta)=\sum_{\sigma\in\lbrace\pm1\rbrace^{V(\Gamma)}}\exp(\beta\sum_{ab}\sigma_a\sigma_b)`$ (сумма по рёбрам; $`J=1`$, $`h=0`$). (а) Доказать, что $`Z_G(\beta)=2^{\lvert V\rvert}(\cosh\beta)^{\lvert E\rvert}\sum_{E'}(\tanh\beta)^{\lvert E'\rvert}`$ по чётным подграфам $`E'\subset E`$ (все степени в $`(V,E')`$ чётны). (б) Доказать, что при $`\tanh\beta=e^{-2\beta^{\ast}}`$

```math
Z_G(\beta)=2^{\lvert V\rvert-1}(\cosh\beta)^{\lvert E\rvert}e^{-\beta^{\ast}\lvert E\rvert}Z_{G^{\ast}}(\beta^{\ast}).
```

(в) Доказать, что $`\sinh2\beta\,\sinh2\beta^{\ast}=1`$ и что $`\beta\mapsto\beta^{\ast}`$ — убывающая инволюция $`(0,\infty)`$ с единственной неподвижной точкой. Вывести соотношение между $`\psi(\beta,0)`$ и $`\psi(\beta^{\ast},0)`$ для $`\mathbb{Z}^2`$ и объяснить, почему при условии, что $`\psi(\cdot,0)`$ неаналитична ровно в одной точке $`(0,\infty)`$, это $`\beta_c=\frac12\log(1+\sqrt2)`$.

**E2.** Нули Ли–Янга для кольца Изинга. В обозначениях D1 пусть $`h\in\mathbb{C}`$; по-прежнему $`Z_N=\mathrm{tr}\,T^N`$, $`T_{\sigma\sigma'}=\exp\left(\beta J\sigma\sigma'+\frac{\beta h}{2}(\sigma+\sigma')\right)`$. (а) Доказать, что $`e^{-N\beta h}Z_N=P_N(z)`$ — многочлен степени $`N`$ от $`z=e^{-2\beta h}`$, и без ссылки на теорему Ли–Янга доказать, что $`Z_N\neq0`$ при $`\mathrm{Re}\,h\neq0`$ (указание: сравнить модули собственных значений $`T`$ с помощью $`\det T`$ и $`\mathrm{tr}\,T`$). (б) Найти все $`N`$ нулей $`P_N`$ явно и доказать, что они лежат на дуге $`2t_0 < \arg z < 2\pi-2t_0`$, где $`\sin t_0=e^{-2\beta J}`$, $`0 < t_0 < \pi/2`$. (в) Что происходит с нулями при $`N\to\infty`$; почему $`\psi`$ аналитична в комплексной окрестности $`h=0`$; что меняется при $`\beta\to\infty`$?

## Карта навыков

| Тема из «Содержания» | Задачи |
|---|---|
| Микроканонический, канонический и большой канонический ансамбли | A1, A2, C1, C4 |
| Энтропия, свободная энергия, вариационный принцип Гиббса | C1, C2 |
| Термодинамический предел, существование удельной свободной энергии, эквивалентность ансамблей | A2, A3, B4, C1, C5 |
| Идеальный газ, теорема о равнораспределении | C2 |
| Квантовые идеальные газы Бозе и Ферми, бозе-эйнштейновская конденсация | A1, C4 |
| Модель Изинга: трансфер-матрица в размерности 1 (контрольная точка) | D1, E2 |
| Модель Изинга: аргумент Пайерлса (контрольная точка) | D2 |
| Двойственность Крамерса–Ванье, решение Онсагера | A7, B1, E1 |
| Теорема Ли–Янга | A8, B5, E2 |
| Теория среднего поля (Кюри–Вейсс), критические показатели | A9, B2, C3 |
| Меры Гиббса на решётке, условия DLR, фазовый переход как неединственность | A4, A5, B1, D2 |
| Корреляционные неравенства Гриффитса и FKG | A6, B3 |
| Ренормгруппа (обзор) | A10 |

Если по теме потеряно больше половины баллов — к ней стоит вернуться:
- ансамбли, энтропия, идеальный газ — Friedli, Velenik «Statistical Mechanics of Lattice Systems», гл. 1; Ландау, Лифшиц, т. 5, главы «Распределение Гиббса» и «Идеальный газ»;
- термодинамический предел — Friedli, Velenik, гл. 3; Ruelle «Statistical Mechanics: Rigorous Results»; Минлос «Введение в математическую статистическую физику»;
- квантовые газы — Ландау, Лифшиц, т. 5, глава «Распределения Ферми и Бозе»;
- одномерная модель Изинга, Пайерлс, GKS и FKG, Ли–Янг — Friedli, Velenik, гл. 3; Baxter «Exactly Solved Models in Statistical Mechanics», гл. 2;
- Крамерс–Ванье и Онсагер — Baxter, гл. 6–7;
- Кюри–Вейсс и критические показатели — Friedli, Velenik, гл. 2; Baxter, гл. 3;
- меры Гиббса и DLR — Friedli, Velenik, гл. 6; Georgii «Gibbs Measures and Phase Transitions», гл. 1–2 (дополнительно к карточке);
- ренормгруппа — Cardy «Scaling and Renormalization in Statistical Physics» (дополнительно к карточке).

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
| 0–39 | Не усвоено | Проверить пререквизиты: части A и C диагностик P1, R2, Q1 (мера Лиувилля) и, для квантовой части, Q2; затем Friedli–Velenik, гл. 1–3 с упражнениями |
| 40–59 | Фрагментарно | По карте навыков выбрать провальные темы; самостоятельно провести вычисления для Кюри–Вейсса (Friedli–Velenik, гл. 2) и одномерного Изинга (Baxter, гл. 2), затем доказательство Пайерлса |
| 60–74 | Рабочий уровень | Можно начинать Q10, параллельно закрывая пробелы; для кинетики критически важны ансамбли, энтропия, вариационный принцип и идеальный газ (на них опираются H-теорема и максвелловские распределения) |
| 75–89 | Уверенно | Можно ставить галочку в plan.md |
| 90–100 | Свободное владение | Переходить к Q10; для глубины — Friedli–Velenik, гл. 5–7 (кластерные разложения, меры Гиббса в бесконечном объёме, теория Пирогова–Синая), Baxter, гл. 7; для связей — большие уклонения и динамика Глаубера (P1, P3), решёточные модели как евклидовы КТП (Q4) |

**Правило галочки:** ставить `[x]` напротив Q9 в plan.md, если итог ≥ 75, в каждой из частей A–D набрано не меньше половины баллов, а обе задачи с пометкой «контрольная точка» (D1 и D2) решены полностью.

**Диагностика по профилю:**
- A высокое, C низкое — язык выучен, но нет навыка счёта: прорешать статсуммы идеального газа, двухуровневой системы, Кюри–Вейсса и квантовых газов.
- C высокое, D низкое — центральные доказательства не собраны: заново пройти Friedli–Velenik, гл. 3 (трансфер-матрица, контуры, построение $`\mu^+`$), записывая доказательства целиком.
- B низкое — нет чувства границ: единственность — это дифференцируемость по $`h`$, а не по $`\beta`$; предел требует условия Ван Хова; GKS и Ли–Янг требуют ферромагнитности.
- E = 0 при остальном ≥ 75 — нормально: двойственность и нули Ли–Янга — техника точно решаемых моделей (Baxter), она понадобится для критического предела (конформная теория поля, SLE).

## Ключ для самопроверки

<details>
<summary>Открыть только после окончания экзамена</summary>

### Часть A

1. $`Z_N=\frac{1}{(2\pi)^{dN}N!}\int_{\Lambda^N\times\mathbb{R}^{dN}}e^{-\beta H_N}dq\,dp < \infty`$ (например, $`U_N`$ ограничен снизу); мера — $`e^{-\beta H_N}`$ с этой нормировкой на $`\Lambda^N\times\mathbb{R}^{dN}`$. $`\Xi=\sum_{N\ge0}e^{\beta\mu N}Z_N`$ (при сходимости), мера на $`\bigsqcup_N\Lambda^N\times\mathbb{R}^{dN}`$: сектор $`N`$ имеет вес $`e^{\beta\mu N}Z_N/\Xi`$, условно на $`N`$ — каноническая мера. Квантовый случай: $`H`$ самосопряжён и $`e^{-\beta H}`$ ядерный, $`\rho_\beta=e^{-\beta H}/\mathrm{tr}\,e^{-\beta H}`$. $`\langle H\rangle=-\partial_\beta\log Z_N`$, $`\mathrm{Var}\,H=\partial^2_\beta\log Z_N`$. Критерии: ансамбли с $`1/N!`$ и ядерностью — 1; формулы — 1.
2. Конечное $`\Omega`$: равномерная мера на $`\lbrace H=E\rbrace`$, $`S=\log\#\lbrace H=E\rbrace`$. Классически ($`E`$ — регулярное значение): мера $`d\sigma/\lvert\nabla H\rvert`$ на $`\lbrace H=E\rbrace`$, $`S(E)`$ — логарифм её массы, $`1/T=S'(E)`$. Изинг: $`s(e)=\lim_{\delta\downarrow0}\lim_n\lvert\Lambda_n\rvert^{-1}\log\#\lbrace\sigma:\lvert H_{\Lambda_n}(\sigma)-e\lvert\Lambda_n\rvert\rvert\le\delta\lvert\Lambda_n\rvert\rbrace`$ существует, вогнута и полунепрерывна сверху; $`\psi(\beta,0)=\sup_e(s(e)-\beta e)`$, $`s(e)=\inf_{\beta\in\mathbb{R}}(\psi(\beta,0)+\beta e)`$ (сопряжение Лежандра–Фенхеля; $`\psi(\beta,0)`$ здесь определено тем же пределом при всех $`\beta\in\mathbb{R}`$, при $`e>0`$ нужны $`\beta < 0`$). Критерии: 1 + 1.
3. Каждая точка лежит во всех $`\Lambda_n`$, начиная с некоторого, и $`\lvert\partial\Lambda_n\rvert/\lvert\Lambda_n\rvert\to0`$, $`\partial\Lambda=\lbrace i\in\Lambda:\exists j\notin\Lambda,\ j\sim i\rbrace`$. Теорема: для любой такой последовательности и любых граничных условий $`\eta_n`$ (включая свободное и периодическое) $`\lim_n\lvert\Lambda_n\rvert^{-1}\log Z^{\eta_n}_{\Lambda_n;\beta,h}`$ существует и не зависит ни от последовательности, ни от граничных условий; $`\psi`$ выпукла по $`h`$ и по $`\beta`$, чётна и липшицева по $`h`$. Критерии: 1 + 1.
4. $`\gamma_\Lambda(\cdot\mid\omega)=\mu^\omega_{\Lambda;\beta,h}`$; $`\mu`$ — мера Гиббса, если при всех конечных $`\Lambda`$, $`A\in\mathcal{F}`$: $`\mu(A\mid\mathcal{F}_{\Lambda^c})(\omega)=\gamma_\Lambda(A\mid\omega)`$ $`\mu`$-п. н., $`\mathcal{F}_{\Lambda^c}=\sigma(\sigma_i:i\notin\Lambda)`$; эквивалентно $`\mu\gamma_\Lambda=\mu`$. $`\mathcal{G}`$ непусто (предельные точки $`\mu^\eta_{\Lambda_n}`$), выпукло, слабо компактно; крайние точки — меры, тривиальные на хвостовой $`\sigma`$-алгебре; всякая мера Гиббса — их смесь. Критерии: 1 + 1.
5. Фазовый переход: $`\lvert\mathcal{G}(\beta,h)\rvert\ge2`$. $`\partial^\pm_h\psi=\beta\langle\sigma_0\rangle^\pm_{\beta,h}`$, и равносильны: $`\lvert\mathcal{G}\rvert=1`$; $`\langle\sigma_0\rangle^+=\langle\sigma_0\rangle^-`$; $`\psi`$ дифференцируема по $`h`$. При $`d\ge2`$: $`0 < \beta_c < \infty`$; единственность при $`h\neq0`$ и при $`h=0`$, $`\beta < \beta_c`$; $`\mu^+\neq\mu^-`$ при $`h=0`$, $`\beta>\beta_c`$. При $`d=1`$ единственность всюду. Критерии: 1 + 1.
6. GKS: $`H=-\sum_{A\subset\Lambda}J_A\sigma_A`$, $`\sigma_A=\prod_{i\in A}\sigma_i`$, все $`J_A\ge0`$ (включая поля, $`\lvert A\rvert=1`$). Тогда $`\langle\sigma_A\rangle\ge0`$ и $`\langle\sigma_A\sigma_B\rangle\ge\langle\sigma_A\rangle\langle\sigma_B\rangle`$, то есть $`\partial\langle\sigma_A\rangle/\partial J_B\ge0`$. FKG: строго положительная $`\mu`$ на $`\lbrace\pm1\rbrace^\Lambda`$ с $`\mu(\sigma\vee\eta)\mu(\sigma\wedge\eta)\ge\mu(\sigma)\mu(\eta)`$; тогда $`\mu(fg)\ge\mu(f)\mu(g)`$ для неубывающих $`f,g`$. Изинг с $`J_{ij}\ge0`$, полями любого знака и любым граничным условием ему удовлетворяет. Критерии: 1 + 1.
7. $`\sinh(2\beta_cJ)=1`$, $`\beta_cJ=\frac12\log(1+\sqrt2)\approx0{,}4407`$; $`m^{\ast}(\beta)=(1-\sinh^{-4}(2\beta J))^{1/8}`$ при $`\beta>\beta_c`$, $`0`$ при $`\beta\le\beta_c`$. $`\psi(\beta,0)`$ (явный двойной интеграл Онсагера) аналитична при $`\beta\neq\beta_c`$, теплоёмкость в $`\beta_c`$ расходится логарифмически. Критерии: $`\beta_c`$ — 1; $`m^{\ast}`$ и аналитичность — 1.
8. $`J_{ij}=J_{ji}\ge0`$ (любые ферромагнитные пары), общее поле $`h`$: $`Z_\Lambda=e^{\beta h\lvert\Lambda\rvert}P(z)`$, $`z=e^{-2\beta h}`$, $`\deg P=\lvert\Lambda\rvert`$. Все нули $`P`$ на $`\lvert z\rvert=1`$, то есть $`Z_\Lambda\neq0`$ при $`\mathrm{Re}\,h\neq0`$. Следствие: $`\lvert\Lambda\rvert^{-1}\log Z_\Lambda`$ аналитичны и локально равномерно ограничены в $`\mathrm{Re}\,h>0`$, по теореме Витали $`\psi`$ аналитична при $`h>0`$ (и $`h < 0`$): перехода при $`h\neq0`$ нет. Критерии: 1 + 1.
9. $`m^{\ast}\asymp(\beta-\beta_c)^{\hat\beta}`$ ($`\beta\downarrow\beta_c`$); $`\chi=\partial_hm\rvert_{h=0}\asymp(\beta_c-\beta)^{-\hat\gamma}`$ ($`\beta\uparrow\beta_c`$); $`m(\beta_c,h)\asymp h^{1/\hat\delta}`$ ($`h\downarrow0`$); $`\xi\asymp\lvert\beta-\beta_c\rvert^{-\nu}`$, где $`m=\beta^{-1}\partial_h\psi`$, $`\xi`$ — скорость экспоненциального убывания усечённой корреляции. Среднее поле: $`\frac12,1,3,\frac12`$; $`d=2`$: $`\frac18,\frac74,15,1`$. Критерии: 1 + 1.
10. Блоки из $`b^d`$ спинов заменяются блок-спинами, $`K'=R_bK`$ — взаимодействие, при котором их распределение гиббсовское; $`R_bR_{b'}=R_{bb'}`$, $`\xi(R_bK)=\xi(K)/b`$. В неподвижной точке $`\xi\in\lbrace0,\infty\rbrace`$, критическая поверхность — её устойчивое многообразие. Собственные значения $`DR_b(K^{\ast})`$: $`b^{y_i}`$, $`y_i>0`$ — релевантные, $`y_i < 0`$ — иррелевантные. Из $`\xi(K^{\ast}+te_t)=b\,\xi(K^{\ast}+b^{y_t}te_t)`$: $`\nu=1/y_t=\log b/\log\lambda_t`$. Универсальность: показатели одинаковы во всём бассейне $`K^{\ast}`$. (Это физический уровень строгости.) Критерии: 1 + 1.

### Часть B

1. **Неверно.** По Онсагеру (A7) $`\psi(\beta,0)`$ аналитична при $`\beta\neq\beta_c`$, но при $`\beta_0J\ge1`$ (D2) $`\mu^+\neq\mu^-`$. Единственность отвечает дифференцируемости по $`h`$ (A5): при $`h=0`$ односторонние производные по $`h`$ равны $`\pm\beta m^{\ast}(\beta)`$.
2. **Верно.** $`\mu_N(m_N=m)=\binom{N}{N(1-m)/2}e^{N\beta Jm^2/2}/Z_N`$, и оценки из C3 дают $`\limsup\frac1N\log\mu_N(m_N\in F)\le\sup_F\varphi-\max\varphi < 0`$ для замкнутого $`F\not\ni\pm m^{\ast}`$ (максимум $`\varphi`$ — ровно в $`\pm m^{\ast}`$). Масса сосредотачивается в малых окрестностях $`\pm m^{\ast}`$, а по симметрии $`\sigma\mapsto-\sigma`$ каждая получает $`\frac12+o(1)`$. (Предел $`\delta_{m^{\ast}}`$ — только в порядке $`\lim_{h\downarrow0}\lim_N`$.)
3. **Верно.** $`\partial_\beta\langle\sigma_0\sigma_x\rangle=J\sum_{\lbrace i,j\rbrace\subset\Lambda}\left(\langle\sigma_0\sigma_x\sigma_i\sigma_j\rangle-\langle\sigma_0\sigma_x\rangle\langle\sigma_i\sigma_j\rangle\right)\ge0`$ по GKS-2. По $`\Lambda`$: в $`\Lambda'`$ поставим $`J`$ на рёбрах внутри $`\Lambda`$ и $`tJ`$ на остальных; при $`t=0`$ получаем $`\langle\sigma_0\sigma_x\rangle^\varnothing_\Lambda`$ (остальные спины независимы), при $`t=1`$ — $`\langle\sigma_0\sigma_x\rangle^\varnothing_{\Lambda'}`$, производная по $`t`$ неотрицательна по GKS-2.
4. **Неверно.** $`B_n=\lbrace-n,\dots,n\rbrace^2`$, $`S_n=\lbrace(k,0):n < k\le n+n^4\rbrace`$, $`\Lambda_n=B_n\cup S_n`$ возрастают и исчерпывают $`\mathbb{Z}^2`$. Между $`B_n`$ и $`S_n`$ одно ребро, и по C5(а) $`\log Z_{\Lambda_n}=O(n^2)+\log2+(n^4-1)\log(2\cosh\beta J)`$: предел равен $`\log(2\cosh\beta J)`$. Но по E1(а) $`Z_{B_n}\ge2^{\lvert B_n\rvert}(\cosh\beta J)^{\lvert E(B_n)\rvert}`$, $`\lvert E(B_n)\rvert/\lvert B_n\rvert\to2`$, так что $`\psi(\beta,0)\ge\log2+2\log\cosh\beta J>\log(2\cosh\beta J)`$. Нарушено условие Ван Хова.
5. **Неверно.** Два спина: $`Z=e^{\beta J}(e^{2\beta h}+e^{-2\beta h})+2e^{-\beta J}=e^{2\beta h+\beta J}(z^2+2az+1)`$, $`a=e^{-2\beta J}`$; корни $`-a\pm\sqrt{a^2-1}`$. При $`J < 0`$ $`a>1`$: корни вещественные, различные, с произведением $`1`$ — не на окружности. (При $`J\ge0`$ они сопряжены и $`\lvert z\rvert=1`$.)

### Часть C

**C1.** (а) $`D(\mu\Vert\mu_\beta)=\sum\mu\log\frac{\mu}{\mu_\beta}=-S(\mu)+\beta\langle H\rangle_\mu+\log Z(\beta)\ge0`$ (Йенсен для строго выпуклой $`x\log x`$), равенство только при $`\mu=\mu_\beta`$. (б) $`U(\beta)=\langle H\rangle_{\mu_\beta}=-(\log Z)'`$, $`U'=-\mathrm{Var}_{\mu_\beta}H < 0`$; $`U\to\min H`$ при $`\beta\to+\infty`$ и $`\to\max H`$ при $`\beta\to-\infty`$, так что $`U`$ — биекция $`\mathbb{R}\to(\min H,\max H)`$. При $`\langle H\rangle_\mu=E`$ по (а) $`S(\mu)\le\log Z(\beta(E))+\beta(E)E=S(\mu_{\beta(E)})`$, равенство только при $`\mu=\mu_{\beta(E)}`$. $`S_{\max}'=-U\beta'+\beta'E+\beta=\beta`$. $`\beta(E) < 0\iff E>U(0)=\lvert\Omega\rvert^{-1}\sum_\omega H(\omega)`$. (в) $`Z=(1+e^{-\beta\varepsilon})^N`$, $`U/N=\varepsilon/(e^{\beta\varepsilon}+1)`$, откуда $`\beta(E)=\frac1\varepsilon\log\frac{\varepsilon-e}{e}`$, $`S_{\max}/N=-p\log p-(1-p)\log(1-p)`$, $`p=e/\varepsilon`$; $`\beta < 0`$ при $`e>\varepsilon/2`$. $`\#\lbrace H=E\rbrace=\binom Nk`$, $`k=E/\varepsilon`$, и по Стирлингу $`\frac1N\log\binom Nk`$ стремится к тому же (эквивалентность ансамблей). Критерии: 2 + 2 + 2.

**C2.** (а) $`\int e^{-\beta\lvert p\rvert^2/2m}\frac{d^3p}{(2\pi)^3}=\left(\frac{m}{2\pi\beta}\right)^{3/2}=\lambda^{-3}`$, интеграл по $`q`$ даёт $`V^N`$. По Стирлингу $`\frac1N\log Z_N\to\log\frac{1}{\rho\lambda^3}+1`$, $`f=-T\left(\log\frac{1}{\rho\lambda^3}+1\right)`$; $`P=\rho T`$; $`\langle H_N\rangle=-\partial_\beta\log Z_N=\frac32NT`$. (б) $`s=\log\frac{1}{\rho\lambda^3}+\frac52`$. Без $`1/N!`$: $`\frac1N\log Z_N=\log(V/\lambda^3)\to\infty`$ — нет экстенсивности (парадокс Гиббса). (в) $`x_i\,\partial_jH\,e^{-\beta H}=-\beta^{-1}x_i\,\partial_je^{-\beta H}`$; по Фубини интегрируем по частям по $`x_j`$, граничные члены исчезают, остаётся $`\beta^{-1}\delta_{ij}\int e^{-\beta H}`$. Газ: $`\langle p_{1a}^2/m\rangle=T`$, откуда $`\frac32T`$. Кристалл: $`H`$ — положительная квадратичная форма от $`x\in\mathbb{R}^{6N}`$, $`\sum x_i\partial_iH=2H`$, поэтому $`2\langle H\rangle=6NT`$. Критерии: 2 + 2 + 2.

**C3.** (а) $`H_N=-N(\frac J2m_N^2+hm_N)`$, $`Z_N=\sum_{k=0}^N\binom Nke^{N\beta(Jm_k^2/2+hm_k)}`$, $`m_k=1-2k/N`$, то есть $`Z_N=2^N\sum_ke^{N\varphi(m_k)+O(\log N)}`$. Сверху: $`(N+1)\max`$; снизу: член с $`m_k`$, ближайшим к точке максимума ($`\varphi`$ непрерывна на $`[-1,1]`$). (б) $`I'=\mathrm{artanh}\to\pm\infty`$ на концах, максимум внутренний, $`\varphi'=\beta(Jm+h)-\mathrm{artanh}\,m=0`$. При $`h=0`$: $`I(m)=\sum_{k\ge1}\frac{m^{2k}}{2k(2k-1)}>\frac{m^2}2`$ при $`m\neq0`$, поэтому при $`\beta J\le1`$ $`\varphi(m) < 0=\varphi(0)`$. При $`\beta J>1`$: $`\varphi''(0)>0`$; $`\tanh(\beta Jm)-m`$ вогнута на $`[0,1]`$, положительна около $`0^+`$ и отрицательна в $`1`$ — один корень $`m^{\ast}>0`$; по чётности максимумы — $`\pm m^{\ast}`$. (в) $`\mathrm{artanh}\,m=m+\frac{m^3}3+O(m^5)`$. Из $`\mathrm{artanh}\,m=\beta Jm`$: $`m^{\ast}\sim\sqrt{3(\beta J-1)}`$, $`\hat\beta=\frac12`$. При $`\beta J=1`$, $`h>0`$ максимум единственен и положителен ($`\varphi(m)-\varphi(-m)=2\beta hm`$), $`\mathrm{artanh}\,m-m=h/J`$ даёт $`m\sim(3h/J)^{1/3}`$, $`\hat\delta=3`$. Критерии: 2 + 2 + 2.

**C4.** (а) Фоковское пространство — тензорное произведение пространств мод, $`H-\mu N=\sum_k(\varepsilon_k-\mu)n_k`$, след факторизуется. Бозоны: геометрические ряды сходятся при $`\mu < \min\varepsilon_k=0`$; фермионы: $`n_k\in\lbrace0,1\rbrace`$, любое $`\mu`$. Произведение сходится, так как $`\sum_ke^{-\beta\varepsilon_k} < \infty`$. $`\langle n_k\rangle=-\beta^{-1}\partial_{\varepsilon_k}\log\Xi=(e^{\beta(\varepsilon_k-\mu)}\mp1)^{-1}`$. (б) $`F(k)=(e^{\beta(\lvert k\rvert^2/2m-\mu)}-1)^{-1}`$ удовлетворяет условию, $`L^{-d}\sum_k\langle n_k\rangle\to(2\pi)^{-d}\int F`$; $`F=\sum_{j\ge1}e^{j\beta\mu}e^{-j\beta\lvert k\rvert^2/2m}`$ и по Тонелли $`(2\pi)^{-d}\int e^{-j\beta\lvert k\rvert^2/2m}dk=\lambda^{-d}j^{-d/2}`$. (в) $`g_s\uparrow`$; $`\sup\rho_3=\zeta(3/2)\lambda^{-3}=:\rho_c`$, $`\zeta(3/2)\approx2{,}612`$; $`g_1(z)=-\log(1-z)\to\infty`$, при $`d=2`$ любая плотность достигается при $`\mu < 0`$ — конденсации нет. При $`\rho>\rho_c`$ в $`d=3`$ ($`\mu_L\uparrow0`$) избыток уходит в основное состояние: $`L^{-3}\langle n_0\rangle\to\rho-\rho_c`$ — бозе-эйнштейновская конденсация. $`T_c=\frac{2\pi}m\left(\frac{\rho}{\zeta(3/2)}\right)^{2/3}`$. Критерии: 2 + 2 + 2 (в (в): значения $`\sup`$ — 1, интерпретация и $`T_c`$ — 1).

**C5.** (а) $`H_{\Lambda_1\cup\Lambda_2}=H_{\Lambda_1}+H_{\Lambda_2}+W`$, $`\lvert W\rvert\le Je(\Lambda_1,\Lambda_2)`$. Второе: $`2^{\lvert\Lambda\rvert}`$ слагаемых, рёбер в $`\Lambda`$ не больше $`d\lvert\Lambda\rvert`$. (б) Куб стороны $`2\ell`$ — это $`2^d`$ кубов стороны $`\ell`$ с $`d(2\ell)^{d-1}`$ рёбрами между ними; по (а) $`\lvert\log Z_{C_{2\ell}}-2^d\log Z_{C_\ell}\rvert\le\beta Jd(2\ell)^{d-1}`$, делим на $`(2\ell)^d`$. (в) $`\ell=2^k`$, $`q=\lfloor n/\ell\rfloor`$: $`C_n`$ содержит $`q^d`$ сдвигов $`C_\ell`$, остаток $`R`$, $`\lvert R\rvert\le d\ell n^{d-1}`$, рёбер между частями $`\le2dn^d/\ell`$. По (а)

<div align="center">

$`\displaystyle \left\lvert\frac{\log Z_{C_n}}{n^d}-\left(\frac{q\ell}{n}\right)^da_k\right\rvert\le\frac{2d\beta J}{\ell}+\frac{d\ell}{n}(\log2+\beta Jd+\beta\lvert h\rvert);`$

</div>

при $`n\to\infty`$ верхний и нижний пределы отличаются от $`a_k`$ не больше чем на $`2d\beta J2^{-k}`$, затем $`k\to\infty`$. (г) $`H^+_{C_n}-H^\varnothing_{C_n}=-J\sum\sigma_i`$ по $`2dn^{d-1}`$ рёбрам наружу, так что разность логарифмов $`\le2\beta Jdn^{d-1}=o(n^d)`$. Критерии: (а) — 1; (б) — 2; (в) — 2; (г) — 1.

### Часть D

**D1.** Схема.
1. (а) $`e^{-\beta H_N}=\prod_iT_{\sigma_i\sigma_{i+1}}`$, $`T_{\sigma\sigma'}=e^{\beta J\sigma\sigma'+\beta h(\sigma+\sigma')/2}`$; сумма по $`\sigma`$ — след. $`\mathrm{tr}\,T=2e^{\beta J}\cosh\beta h`$, $`\det T=2\sinh2\beta J>0`$:

<div align="center">

$`\displaystyle \lambda_\pm=e^{\beta J}\cosh\beta h\pm\sqrt{e^{2\beta J}\sinh^2\beta h+e^{-2\beta J}},\qquad \lambda_+>\lambda_->0.`$

</div>

2. (б) $`Z_N=\lambda_+^N(1+(\lambda_-/\lambda_+)^N)`$, $`\psi=\log\lambda_+`$; подкоренное выражение положительно и аналитично — $`\psi`$ вещественно-аналитична по $`h`$ (и по $`\beta`$). Свободное условие: $`Z^\varnothing_N=\langle u,T^{N-1}u\rangle`$, $`u_\sigma=e^{\beta h\sigma/2}`$; $`v_+`$ положителен (Перрон–Фробениус), $`\langle u,v_+\rangle>0`$, предел тот же.
3. (в) $`\langle\sigma_1\rangle_N=(N\beta)^{-1}\partial_h\log Z_N=\beta^{-1}\partial_h\log\lambda_++O((\lambda_-/\lambda_+)^{N-1})`$, и $`m(\beta,h)=\sinh\beta h/\sqrt{\sinh^2\beta h+e^{-4\beta J}}`$; $`m`$ непрерывна и $`m(\beta,0)=0`$: $`\lim_{h\downarrow0}m=0`$ при каждом $`\beta < \infty`$.
4. (г) $`v_+=(\cos\phi,\sin\phi)`$, $`v_-=(-\sin\phi,\cos\phi)`$, $`S=\mathrm{diag}(1,-1)`$; $`\langle\sigma_0\rangle_N\to\cos2\phi=m`$, $`\langle\sigma_0\sigma_r\rangle_N=\frac{\mathrm{tr}(ST^rST^{N-r})}{\mathrm{tr}\,T^N}\to\cos^22\phi+\sin^22\phi\,(\lambda_-/\lambda_+)^r`$. Итак, $`A=1-m^2=\frac{e^{-4\beta J}}{\sinh^2\beta h+e^{-4\beta J}}`$, $`\xi=1/\log(\lambda_+/\lambda_-) < \infty`$. При $`h=0`$: $`\lambda_\pm=2\cosh\beta J,2\sinh\beta J`$, $`\langle\sigma_0\sigma_r\rangle=(\tanh\beta J)^r`$, $`\xi=-1/\log\tanh\beta J\sim\frac12e^{2\beta J}`$.
5. (д) При $`h=0`$: $`(T^k)_{+\pm}=\frac{c^k\pm s^k}{2}`$, $`c=2\cosh\beta J`$, $`s=2\sinh\beta J`$. С $`k=n+1`$ шагами до каждой границы

<div align="center">

$`\displaystyle \langle\sigma_0\rangle^+_n=\frac{(T^k)_{++}^2-(T^k)_{+-}^2}{(T^k)_{++}^2+(T^k)_{+-}^2}=\frac{2t^{n+1}}{1+t^{2n+2}}\to0,\qquad t=\tanh\beta J < 1.`$

</div>

По симметрии $`\langle\sigma_0\rangle^-_n=-\langle\sigma_0\rangle^+_n`$, поэтому $`\langle\sigma_0\rangle^\pm_{\beta,0}=0`$ и $`\lvert\mathcal{G}(\beta,0)\rvert=1`$; при $`h\neq0`$ единственность следует из дифференцируемости $`\psi=\log\lambda_+`$ по $`h`$ (A5; $`\lambda_+`$ — простое собственное значение). Перехода при $`T>0`$ нет; при $`\beta\to\infty`$ $`\xi\to\infty`$ — «переход при $`T=0`$».

Критерии: (а) — 2; (б) — 2; (в) — 2; (г) — 2; (д) — 2. КТ засчитывается, если (а)–(в) и (д) решены полностью, а в (г) верно найдены $`\xi=1/\log(\lambda_+/\lambda_-)`$ и ответ при $`h=0`$.

**D2.** Схема.
1. (а) $`\Gamma(\omega)`$ — двойственные рёбра, пересекающие пары $`\lbrace i,j\rbrace`$ с $`\omega_i\neq\omega_j`$ (все такие пары лежат в $`\mathcal{E}^b_{\Lambda_n}`$). Вокруг плакета смен знака чётное число, так что степени $`0,2,4`$; в вершинах степени $`4`$ рёбра соединяются попарно по фиксированному правилу. Тогда $`\Gamma(\omega)`$ однозначно распадается на рёберно-непересекающиеся простые замкнутые ломаные — контуры. Каждая несогласованная пара даёт $`+J`$ вместо $`-J`$, отсюда формула для $`H^+`$. Если $`\omega_0=-1`$, то на луче $`\lbrace(x,0):x\ge0\rbrace`$ спин меняется с $`-1`$ на $`+1`$, луч пересекает $`\Gamma(\omega)`$ нечётное число раз, значит, некоторый контур — нечётное число раз, и по теореме Жордана $`0\in\mathrm{int}\,\gamma`$.
2. (б) $`\Omega_\gamma=\lbrace\omega:\gamma\ \text{— контур}\ \omega\rbrace`$, $`\tau_\gamma`$ меняет знаки в $`\mathrm{int}\,\gamma`$. Узлы $`\mathrm{int}\,\gamma`$ лежат в $`\Lambda_n`$ (дополнение $`\Lambda_n`$ связно и неограниченно, а $`\gamma`$ пересекает только пары из $`\mathcal{E}^b`$), так что $`\tau_\gamma\omega\in\Omega^+_{\Lambda_n}`$. Согласованность меняется ровно на парах, пересекающих $`\gamma`$ (все были несогласованы): $`H^+(\tau_\gamma\omega)=H^+(\omega)-2J\lvert\gamma\rvert`$. $`\tau_\gamma`$ — инволюция, поэтому $`\mu^+_n(\Omega_\gamma)=e^{-2\beta J\lvert\gamma\rvert}\sum_{\omega\in\Omega_\gamma}e^{-\beta H^+(\tau_\gamma\omega)}/Z^+\le e^{-2\beta J\lvert\gamma\rvert}`$.

3. (в) Контур длины $`\ell`$ вокруг $`0`$ пересекает положительную полуось в точке $`(k+\frac12,0)`$ и отрицательную — где-то ещё; обе дуги между ними длиннее $`k+\frac12`$, поэтому $`k+\frac12\le\ell/2`$ — не больше $`\ell/2`$ вариантов. Далее обход от этого ребра вверх: каждое из $`\ell-1`$ следующих рёбер — не более $`3`$ вариантов. Длины чётны, $`\ell\ge4`$. При $`x=3e^{-2\beta J} < 1`$

<div align="center">

$`\displaystyle \mu^+_n(\sigma_0=-1)\le\sum_{\ell\ge4\ \text{чётн.}}\frac\ell2\,3^{\ell-1}e^{-2\beta J\ell}=\frac13\sum_{k\ge2}kx^{2k}=\frac{x^4(2-x^2)}{3(1-x^2)^2}=:\varepsilon(\beta).`$

</div>

При $`\beta J\ge1`$: $`e^2>7`$, $`x^2 < 9/49`$, $`\varepsilon`$ возрастает по $`x^2`$, и $`\varepsilon < \frac{2\cdot81}{3\cdot1600}=0{,}03375`$, так что $`\langle\sigma_0\rangle^+_{\Lambda_n}=1-2\mu^+_n(\sigma_0=-1)\ge0{,}93`$. (Точно: $`\varepsilon(1/J)\approx0{,}024`$; $`\varepsilon < \frac12`$ при $`\beta J>0{,}723`$. С грубым подсчётом $`4\ell\cdot3^{\ell-1}`$ сумма при $`\beta J=1`$ меньше $`0{,}29`$: $`\langle\sigma_0\rangle^+>0`$, но не $`0{,}9`$ — минус 1 балл, КТ засчитывается.)
4. (г) $`\Omega`$ компактно, поэтому $`\mu^+_{n_k}\Rightarrow\mu^+_\beta`$ по подпоследовательности. При $`\Lambda\subset\Lambda_n`$ согласованность даёт $`\mu^+_n\gamma_\Lambda=\mu^+_n`$; для локальной $`f`$ функция $`\gamma_\Lambda f`$ локальна (ближайшие соседи), значит непрерывна, и в пределе $`\mu^+_\beta\gamma_\Lambda f=\mu^+_\beta f`$: $`\mu^+_\beta\in\mathcal{G}(\beta,0)`$. $`\sigma_0`$ непрерывна, $`\mu^+_\beta(\sigma_0)\ge0{,}93`$; образ $`\mu^-_\beta`$ при глобальном перевороте — тоже мера Гиббса (симметрия при $`h=0`$), $`\mu^-_\beta(\sigma_0)\le-0{,}93`$. Итак, $`\mu^+\neq\mu^-`$, $`m^{\ast}(\beta)>0`$ при $`\beta J\ge1`$ и $`\beta_c(2)\le1/J`$.

Критерии: (а) — 2 (контуры и энергия — 1, контур вокруг $`0`$ — 1); (б) — 3 (отображение, граничное условие и инъективность — 2, энергия — 1); (в) — 3 (подсчёт — 2, явная оценка — 1); (г) — 2. Для засчитывания КТ нужны все пункты, в (в) — явное $`\beta`$, при котором $`\langle\sigma_0\rangle^+_{\Lambda_n}`$ равномерно по $`n`$ отделено от нуля.

### Часть E

**E1.** (а) $`e^{\beta\sigma\sigma'}=\cosh\beta\,(1+\sigma\sigma'\tanh\beta)`$; раскрываем произведение по $`E`$, и $`\sum_\sigma\prod_v\sigma_v^{\deg_{E'}v}`$ равна $`2^{\lvert V\rvert}`$ для чётного $`E'`$ и $`0`$ иначе. (б) Для $`\tau\in\lbrace\pm1\rbrace^{V^{\ast}}`$ пусть $`E'(\tau)`$ — рёбра, по разные стороны которых $`\tau`$ различны. Грани вокруг вершины образуют цикл, смен знака на нём чётное число — $`E'(\tau)`$ чётен. $`\tau\mapsto E'(\tau)`$ — гомоморфизм в группу чётных подграфов по $`\triangle`$; ядро — постоянные $`\tau`$ ($`G^{\ast}`$ связен); сюръективность: чётный подграф — объединение рёберно-непересекающихся простых циклов, а для цикла $`C`$ по Жордану $`\tau_C=-1`$ внутри и $`+1`$ снаружи даёт $`E'(\tau_C)=C`$. Значит, $`\sum_{E'}x^{\lvert E'\rvert}=\frac12\sum_\tau x^{\lvert E'(\tau)\rvert}`$, а при $`x=e^{-2\beta^{\ast}}`$ имеем $`x^{\mathbf{1}[\tau_a\neq\tau_b]}=e^{-\beta^{\ast}}e^{\beta^{\ast}\tau_a\tau_b}`$ и $`\sum_\tau x^{\lvert E'(\tau)\rvert}=e^{-\beta^{\ast}\lvert E\rvert}Z_{G^{\ast}}(\beta^{\ast})`$. (в) $`t=\tanh\beta`$: $`\sinh2\beta=\frac{2t}{1-t^2}`$, $`\sinh2\beta^{\ast}=\frac{1-t^2}{2t}`$. Соотношение симметрично, $`\beta^{\ast}`$ убывает; неподвижная точка $`\sinh2\beta=1`$, $`\beta=\frac12\log(1+\sqrt2)`$. Для $`G=\Lambda_n`$ граф $`G^{\ast}`$ — меньший квадрат плюс внешняя вершина (граничное условие «$`+`$»). Так как $`\lvert V\rvert\sim\lvert V^{\ast}\rvert\sim N`$, $`\lvert E\rvert\sim2N`$ и предел не зависит от граничного условия (C5(г)):

<div align="center">

$`\displaystyle \psi(\beta,0)-\log2-2\log\cosh\beta=\psi(\beta^{\ast},0)-2\beta^{\ast}.`$

</div>

$`\log\cosh\beta`$ и $`\beta^{\ast}(\beta)`$ аналитичны, поэтому $`\psi`$ неаналитична в $`\beta`$ тогда и только тогда, когда в $`\beta^{\ast}`$; единственная особая точка неподвижна. Критерии: (а) — 2; (б) — 3 (чётность — 1, двулистность — 1, веса — 1); (в) — 2.

**E2.** (а) $`\sum\sigma_i=N-2k`$, $`k`$ — число минусов, так что $`e^{-N\beta h}Z_N=\sum_\sigma e^{\beta J\sum\sigma_i\sigma_{i+1}}z^{k(\sigma)}`$, старший и младший коэффициенты $`e^{N\beta J}`$. $`Z_N=\lambda_1^N+\lambda_2^N`$, $`\lambda_1\lambda_2=2\sinh2\beta J=:P\in(0,e^{2\beta J})`$, $`\lambda_1+\lambda_2=2e^{\beta J}\cosh\beta h`$. Если $`\lvert\lambda_1\rvert=\lvert\lambda_2\rvert`$, то $`\lambda_2=P/\lambda_1=\bar\lambda_1`$, $`\cosh\beta h`$ вещественен и $`\lvert\cosh\beta h\rvert\le\sqrt P\,e^{-\beta J} < 1`$. Но при $`h=a+ib`$, $`a\neq0`$, вещественность $`\cosh\beta a\cos\beta b+i\sinh\beta a\sin\beta b`$ требует $`\sin\beta b=0`$, и тогда $`\lvert\cosh\beta h\rvert=\cosh\beta a>1`$. Значит, при $`\mathrm{Re}\,h\neq0`$ $`\lvert Z_N\rvert\ge\lvert\lambda_1\rvert^N-\lvert\lambda_2\rvert^N>0`$. (б) Пусть $`h=i\theta`$, $`t=\beta\theta`$, $`z=e^{-2it}`$. При $`\sin^2t\le e^{-4\beta J}`$ $`\lambda_{1,2}`$ вещественны одного знака и либо различны по модулю, либо равны ($`Z_N=2\lambda^N`$): нулей нет. При $`\sin^2t>e^{-4\beta J}`$: $`\lambda_{1,2}=\sqrt Pe^{\pm i\phi}`$, $`\cos\phi=e^{\beta J}\cos t/\sqrt P`$, $`Z_N=2P^{N/2}\cos N\phi`$, и $`\phi`$ монотонно пробегает $`(0,\pi)`$, когда $`t`$ пробегает $`(t_0,\pi-t_0)`$. Нули: $`z_k=e^{-2it_k}`$, где $`e^{\beta J}\cos t_k=\sqrt{2\sinh2\beta J}\cos\frac{(2k+1)\pi}{2N}`$, $`k=0,\dots,N-1`$; это $`N`$ различных точек дуги, то есть все нули $`P_N`$. (в) При $`N\to\infty`$ нули всюду плотно заполняют дугу, но не подходят к $`z=1`$ ближе угла $`2t_0=2\arcsin e^{-2\beta J}`$. При $`h=0`$ $`\lambda_-/\lambda_+=\tanh\beta J < 1`$, поэтому в малой комплексной окрестности $`U`$ точки $`0`$ $`\lambda_\pm`$ аналитичны, $`\lvert\lambda_-/\lambda_+\rvert\le q < 1`$ и $`\frac1N\log Z_N\to\log\lambda_+`$ равномерно на $`U`$: $`\psi`$ аналитична. При $`\beta\to\infty`$ $`t_0\to0`$: щель закрывается, нули зажимают $`z=1`$ — переход при $`T=0`$. Критерии: (а) — 3 (многочлен — 1, модули — 2); (б) — 3; (в) — 2.

</details>
