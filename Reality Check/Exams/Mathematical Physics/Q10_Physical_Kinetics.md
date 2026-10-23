# Q10. Физическая кинетика — диагностика

> **Код в плане:** [Q10](../../PLAN.md#q10) · **Время:** ≈ 220 минут ([расширенный экзамен](../../README.md#physics)) · **Максимум:** 100 баллов · **Этап плана:** 4
>
> **Требует:** Q9, D3, P3; R5 желательно. **Можно пользоваться:** только бумагой и ручкой (никаких книг, конспектов, интернета, CAS).

## Как проходить

1. Засечь 220 минут или сдавать в два захода: части A–C (125 минут), затем D–E (95 минут); подробнее — в [особых правилах для физики](../../README.md#physics). Ориентировочное время на части указано в заголовках; переходить к следующей части можно в любой момент.
2. Писать решения полностью, как на письменном экзамене. «Понятно, как делать» без записи — 0 баллов.
3. Ключ в конце файла открывать только после окончания времени. Проверять себя строго, по критериям из ключа.
4. Записать баллы по частям в таблицу результатов в конце и прочитать интерпретацию.

Соглашения: если не сказано иное, $`x\in\mathbb{R}^3`$ или $`\mathbb{T}^3=\mathbb{R}^3/\mathbb{Z}^3`$, $`v\in\mathbb{R}^3`$; масса частицы и постоянная Больцмана равны $`1`$, температура $`\theta`$ — в единицах энергии. $`M_{\rho,u,\theta}(v)=\rho(2\pi\theta)^{-3/2}e^{-\lvert v-u\rvert^2/(2\theta)}`$ — максвеллиан; поля функции $`f\ge0`$: $`\rho=\int f\,dv`$, $`\rho u=\int vf\,dv`$, $`3\rho\theta=\int\lvert v-u\rvert^2f\,dv`$. Оператор столкновений ($`\sigma`$-представление):

```math
Q(f,f)(v)=\int_{\mathbb{R}^3}\int_{S^2}B\left(\lvert v-v_*\rvert,\cos\theta\right)\left(f'f'_*-ff_*\right)d\sigma\,dv_*,\qquad v'=\frac{v+v_*}2+\frac{\lvert v-v_*\rvert}2\sigma,\quad v'_*=\frac{v+v_*}2-\frac{\lvert v-v_*\rvert}2\sigma,
```

где $`f'=f(v')`$, $`f'_*=f(v'_*)`$, $`f_*=f(v_*)`$, $`k=\frac{v-v_*}{\lvert v-v_*\rvert}`$, $`\cos\theta=k\cdot\sigma`$, $`d\sigma`$ — мера площади, $`B\ge0`$ измеримо. Уравнение Больцмана: $`\partial_tf+v\cdot\nabla_xf=Q(f,f)`$. «Гауссовы оценки»: $`f`$ гладкая, $`ce^{-A\lvert v\rvert^2}\le f\le Ce^{-a\lvert v\rvert^2}`$ (то же сверху для производных, равномерно по $`x`$), и $`\int_{S^2}B(r,\cos\theta)d\sigma\le C(1+r)`$; тогда все интегралы сходятся, а дифференцирование под интегралом и интегрирование по частям законны — это не проверять. $`H(f)=\iint f\log f\,dx\,dv`$; $`\hat f(k)=\int e^{-ikx}f\,dx`$, $`\tilde F(p)=\int_0^\infty e^{-pt}F(t)dt`$; $`W_t`$ — броуновское движение.

## Часть A. Определения и формулировки (≈ 35 мин, 20 баллов)

Дать точные определения / сформулировать теоремы полностью, со всеми условиями. 10 пунктов по 2 балла.

1. $`N`$ частиц в $`\mathbb{R}^3`$ с гамильтонианом $`\sum_i\frac12\lvert v_i\rvert^2+\sum_{i < j}\Phi(x_i-x_j)`$, $`\Phi`$ чётен. $`N`$-частичная функция распределения и маргиналы $`f_N^{(s)}`$. Вывести из уравнения Лиувилля первое уравнение иерархии ББГКИ и формально получить из него уравнение Власова в масштабе $`\Phi=\frac1N\Phi_0`$. Какое предположение о $`f_N^{(2)}`$ для этого нужно?
2. Предел Больцмана–Грэда для твёрдых сфер диаметра $`\varepsilon`$: соотношение между $`N`$ и $`\varepsilon`$ и его смысл (длина свободного пробега). Теорема Ланфорда: условия на начальные данные, утверждение, интервал времени, сечение $`B`$ в предельном уравнении.
3. Проверить, что $`v'+v'_*=v+v_*`$ и $`\lvert v'\rvert^2+\lvert v'_*\rvert^2=\lvert v\rvert^2+\lvert v_*\rvert^2`$. Сечения твёрдых сфер и максвелловских молекул. Обрезание Грэда и разложение $`Q=Q^+-Q^-`$ (формула для $`Q^-`$).
4. Инварианты столкновений: определение и теорема об их описании (условия регулярности и размерности). Какие локальные законы сохранения из этого следуют?
5. H-теорема для неоднородного уравнения Больцмана: функционал, производство энтропии $`D(f)`$, утверждение, случай $`D(f)=0`$. Что здесь доказано строго и для каких классов решений?
6. Линеаризованный оператор Больцмана около $`M=M_{1,0,1}`$ ($`f=M(1+h)`$): формула для $`Lh`$, пространство, где он симметричен, знак, ядро. Структура $`L=K-\nu(v)`$ при обрезании; спектральная щель для твёрдых сфер.
7. Модель BGK: уравнение, $`M[f]`$. Какие свойства уравнения Больцмана она сохраняет и в чём её дефект как модели одноатомного газа (число Прандтля)?
8. Система Власова–Пуассона в $`\mathbb{R}^3\times\mathbb{R}^3`$ (плазма и гравитация): уравнения, сохраняющиеся величины (включая функционалы Казимира), теорема о глобальных классических решениях.
9. Гидродинамические пределы: уравнение Больцмана с числом Кнудсена $`\varepsilon`$; разложение Гильберта (порядки $`\varepsilon^{-1}`$ и $`\varepsilon^0`$); масштаб, дающий несжимаемые уравнения Навье–Стокса; строгие результаты (Caflisch; Golse–Saint-Raymond) без деталей.
10. Уравнение Крамерса с потенциалом $`V(x)`$, его равновесие и запись $`\partial_th+\mathcal{L}h=0`$, $`\mathcal{L}=A^{\ast}A+B`$. Гипокоэрцитивность (определение по Виллани); почему $`\mathcal{L}`$ не коэрцитивен и какой коммутатор «чинит» вырожденность?

## Часть B. Верно или неверно? (≈ 25 мин, 15 баллов)

Для каждого утверждения ответить «верно» или «неверно» и **обосновать**: короткое доказательство или контрпример. Ответ без обоснования — 0 баллов. 5 пунктов по 3 балла.

1. Пусть размерность скоростей $`d=1`$ ($`v\in\mathbb{R}`$, $`\sigma\in S^0=\lbrace\pm1\rbrace`$ со считающей мерой, формулы для $`v',v'_*`$ — те же), $`B>0`$. Тогда, как и при $`d=3`$, непрерывная положительная $`f`$ с гауссовыми оценками удовлетворяет $`Q(f,f)=0`$, только если $`f`$ — максвеллиан.
2. Пусть $`\tau>0`$, $`f`$ — гладкое положительное решение модели BGK $`\partial_tf+v\cdot\nabla_xf=\tau^{-1}(M[f]-f)`$ на $`\mathbb{T}^3\times\mathbb{R}^3`$ с гауссовыми оценками ($`M[f]`$ — локальный максвеллиан с теми же $`\rho,u,\theta`$, что у $`f`$). Тогда $`H(f(t))`$ не возрастает.
3. Если $`(\rho,u,\theta)`$ — гладкое решение уравнений Эйлера сжимаемого одноатомного газа ($`\rho,\theta>0`$, давление $`p=\rho\theta`$), то локальный максвеллиан $`f(t,x,v)=M_{\rho(t,x),u(t,x),\theta(t,x)}(v)`$ — решение уравнения Больцмана.
4. Пусть $`f_0\in C_c^\infty(\mathbb{T}\times\mathbb{R})`$, $`\mathbb{T}=\mathbb{R}/2\pi\mathbb{Z}`$, $`f(t,x,v)=f_0(x-vt,v)`$ — решение свободного переноса, $`\rho(t,x)=\int f\,dv`$, $`\bar\rho`$ — среднее $`\rho`$ по $`x`$ (не зависит от $`t`$). Тогда $`\sup_x\lvert\rho(t,x)-\bar\rho\rvert=O(t^{-n})`$ для каждого $`n`$, но, вообще говоря (для некоторого $`f_0\ge0`$), не $`O(e^{-at})`$ ни при каком $`a>0`$.
5. Пусть $`\mu=(2\pi)^{-3/2}e^{-v^2/2}dx\,dv`$ — вероятностная мера на $`\mathbb{T}\times\mathbb{R}`$ ($`\mathbb{T}`$ — как в B4), $`Lh=-v\partial_xh+\partial_v^2h-v\partial_vh`$ (генератор уравнения Крамерса без потенциала в переменной $`h=f/\mu`$). Тогда существует $`\kappa>0`$, такое что $`\langle-Lh,h\rangle_{L^2(\mu)}\ge\kappa\left\lVert h-\int h\,d\mu\right\rVert_{L^2(\mu)}^2`$ для всех гладких $`h`$, ограниченных вместе со всеми производными.

## Часть C. Стандартные задачи (≈ 65 мин, 30 баллов)

Вычисления и рутинные доказательства, которые должен уверенно делать каждый, кто прошёл курс. 5 задач по 6 баллов.

**C1.** Моменты и уравнения Эйлера. Пусть $`f`$ — решение уравнения Больцмана с гауссовыми оценками. (а) Пользуясь тем, что $`\int Q(f,f)\varphi\,dv=0`$ для $`\varphi=1,v_i,\lvert v\rvert^2`$, вывести локальные законы сохранения; выразить потоки через $`\rho,u`$, тензор давления $`P=\int(v-u)\otimes(v-u)f\,dv`$ и поток тепла $`q=\int(v-u)\frac{\lvert v-u\rvert^2}2f\,dv`$. (б) Вычислить $`P`$ и $`q`$ для $`f=M_{\rho,u,\theta}`$. (в) Выписать замкнутую систему (уравнения Эйлера), найти показатель адиабаты $`\gamma`$ ($`\rho e=p/(\gamma-1)`$) и, линеаризовав около покоя $`(\rho_0,0,\theta_0)`$, скорость звука.

**C2.** Максвелловские молекулы. Пусть $`B=b(\cos\theta)`$, $`\int_{S^2}b\,d\sigma<\infty`$, $`\Lambda=\int_{S^2}b(k\cdot\sigma)\left(1-(k\cdot\sigma)^2\right)d\sigma`$ (не зависит от $`k`$), и $`f`$ — гладкое пространственно-однородное решение с гауссовыми оценками, $`\int f\,dv=\rho`$, $`\int vf\,dv=0`$. Можно пользоваться слабой формой $`\int Q(f,f)\varphi=\frac12\iint ff_*\int_{S^2}B\left(\varphi'+\varphi'_*-\varphi-\varphi_*\right)d\sigma\,dv_*\,dv`$. (а) Для $`\varphi(v)=v^{\mathsf T}Av`$, $`A`$ симметрична со следом $`0`$, доказать, что $`\varphi'+\varphi'_*-\varphi-\varphi_*=\frac12\lvert v-v_*\rvert^2\left(\sigma^{\mathsf T}A\sigma-k^{\mathsf T}Ak\right)`$. (б) Доказать, что $`\int_{S^2}b(k\cdot\sigma)\left(\sigma^{\mathsf T}A\sigma-k^{\mathsf T}Ak\right)d\sigma=-\frac32\Lambda\,k^{\mathsf T}Ak`$. (в) Вывести, что $`\Pi(t)=\int\left(v\otimes v-\frac13\lvert v\rvert^2I\right)f\,dv`$ удовлетворяет $`\Pi(t)=e^{-\lambda t}\Pi(0)`$, найти $`\lambda`$ и сравнить с однородной моделью BGK с постоянным $`\tau`$ (её решение найти явно).

**C3.** Чепмен–Энског для BGK. Рассмотрим $`\partial_tf+v\cdot\nabla_xf=\tau^{-1}(M[f]-f)`$ с малым постоянным $`\tau`$. Формально $`f=M+\tau f^{(1)}+O(\tau^2)`$, $`M=M_{\rho,u,\theta}`$, $`f^{(1)}=-(\partial_t+v\cdot\nabla_x)M`$, где $`\partial_t\rho,\partial_tu,\partial_t\theta`$ вычислены по уравнениям Эйлера (C1). (а) Доказать, что $`\int f^{(1)}\varphi\,dv=0`$ для $`\varphi=1,v_i,\lvert v\rvert^2`$. (б) Течение сдвига: в данный момент $`u=(U(x_2),0,0)`$, $`\rho,\theta`$ постоянны. Найти $`f^{(1)}`$ и доказать, что $`P_{12}=-\mu U'+O(\tau^2)`$, где $`\mu=\rho\theta\tau`$. (в) Теплопроводность: $`u=0`$, $`\theta=\theta(x_2)`$, $`\rho\theta=p=\mathrm{const}`$. Доказать, что $`q_2=-\kappa\theta'+O(\tau^2)`$, найти $`\kappa`$ и число Прандтля $`\mathrm{Pr}=c_p\mu/\kappa`$, $`c_p=\frac52`$.

**C4.** Уравнение Фоккера–Планка $`\partial_tp=\nabla\cdot(\nabla p+p\nabla V)`$ на $`\mathbb{R}^n`$, $`V`$ гладкий, $`\gamma=e^{-V}`$ — вероятностная плотность, $`p`$ — гладкое положительное решение (интегрирования по частям законны). (а) Доказать, что $`\frac{d}{dt}\int p\log\frac p\gamma\,dx=-\int p\left\lvert\nabla\log\frac p\gamma\right\rvert^2dx`$; вывести, что $`\gamma`$ — единственная стационарная плотность в этом классе. (б) Для $`h=p/\gamma`$ найти уравнение, доказать $`\frac{d}{dt}\lVert h-1\rVert_{L^2(\gamma)}^2=-2\int\lvert\nabla h\rvert^2\gamma\,dx`$ и вывести экспоненциальную сходимость, если $`\gamma`$ удовлетворяет неравенству Пуанкаре $`\mathrm{Var}_\gamma(g)\le C_P\int\lvert\nabla g\rvert^2d\gamma`$. (в) Для $`n=1`$, $`V=\frac{x^2}2+\frac12\log2\pi`$ доказать неравенство Пуанкаре с $`C_P=1`$ через многочлены Эрмита (их полноту в $`L^2(\gamma)`$ можно использовать) и показать, что скорость $`e^{-t}`$ в (б) неулучшаема.

**C5.** Ланжевен и Эйнштейн. Частица массы $`m`$ на прямой: $`dx_t=v_tdt`$, $`dv_t=-\gamma v_tdt+\sqrt{2\gamma\theta/m}\,dW_t`$, $`\gamma,\theta>0`$. (а) Решить уравнение для $`v_t`$; найти закон $`v_t`$ при детерминированном $`v_0`$ и его предел; выписать уравнение Фоккера–Планка для плотности $`v_t`$ и проверить стационарность распределения Максвелла. (б) Пусть $`v_0\sim N(0,\theta/m)`$ не зависит от $`W`$. Найти $`\mathbb{E}\,v_sv_t`$ и $`\mathbb{E}(x_t-x_0)^2`$; вывести $`\mathbb{E}(x_t-x_0)^2\sim2Dt`$ при $`t\to\infty`$ с $`D=\frac{\theta}{m\gamma}`$ и найти асимптотику при $`t\to0`$. (в) Добавим постоянную силу: $`dv_t=(F/m-\gamma v_t)dt+\sqrt{2\gamma\theta/m}\,dW_t`$. Найти $`\lim\mathbb{E}\,v_t/F`$ (подвижность), проверить соотношение Эйнштейна $`D=\theta\cdot(\text{подвижность})`$ и формулу Грина–Кубо $`D=\int_0^\infty\mathbb{E}\,v_0v_t\,dt`$. Что здесь выражает флуктуационно-диссипационная теорема?

## Часть D. Ключевые доказательства (≈ 55 мин, 20 баллов)

Доказать центральные теоремы курса. Сюда входит контрольная точка из plan.md. 2 задачи по 10 баллов. Контрольная точка состоит из двух пунктов, поэтому пометку несут обе задачи.

**D1.** *(контрольная точка)* H-теорема и равновесия. Пусть $`B>0`$ на $`(0,\infty)\times(-1,1)`$ и $`\int_{S^2}B(r,\cos\theta)d\sigma\le C(1+r)`$; $`f\in C^1(\mathbb{R}^3)`$ положительна и $`ce^{-A\lvert v\rvert^2}\le f(v)\le Ce^{-a\lvert v\rvert^2}`$.

(а) Доказать, что для непрерывной $`\varphi`$ с $`\lvert\varphi(v)\rvert\le C(1+\lvert v\rvert^2)`$

```math
\int_{\mathbb{R}^3}Q(f,f)\varphi\,dv=-\frac14\int_{\mathbb{R}^3}\int_{\mathbb{R}^3}\int_{S^2}B\left(f'f'_*-ff_*\right)\left(\varphi'+\varphi'_*-\varphi-\varphi_*\right)d\sigma\,dv_*\,dv.
```

Без доказательства можно использовать, что отображение $`(v,v_*,\sigma)\mapsto(v',v'_*,k)`$ — инволюция множества $`\lbrace v\neq v_*\rbrace\times S^2`$, сохраняющая меру $`dv\,dv_*\,d\sigma`$; всё остальное (в частности, поведение $`B`$) проверить.

(б) Вывести H-теорему: для пространственно-однородного гладкого положительного решения с гауссовыми оценками $`\frac{d}{dt}\int f\log f\,dv=-D(f)\le0`$; выписать $`D(f)`$ и доказать его неотрицательность. Как меняется рассуждение для решений на $`\mathbb{T}^3\times\mathbb{R}^3`$?

(в) Доказать, что $`Q(f,f)=0\iff D(f)=0\iff\log f`$ — инвариант столкновений, то есть $`\log f(v')+\log f(v'_*)=\log f(v)+\log f(v_*)`$ для всех $`v,v_*\in\mathbb{R}^3`$, $`\sigma\in S^2`$.

(г) Доказать: если $`\varphi\in C^1(\mathbb{R}^3)`$ — инвариант столкновений, то $`\varphi(v)=a+b\cdot v+c\lvert v\rvert^2`$. Указание: функция $`\sigma\mapsto\varphi(V+r\sigma)+\varphi(V-r\sigma)`$ постоянна на $`S^2`$. Вывести, что $`Q(f,f)=0`$ тогда и только тогда, когда $`f=M_{\rho,u,\theta}`$, и выразить $`\rho,u,\theta`$ через $`a,b,c`$.

**D2.** *(контрольная точка)* Затухание Ландау. Электроны на неподвижном нейтрализующем ионном фоне, безразмерные единицы (заряд электрона $`-1`$, масса $`1`$, $`\varepsilon_0=1`$): $`x\in\mathbb{T}_L=\mathbb{R}/L\mathbb{Z}`$, $`v\in\mathbb{R}`$,

```math
\partial_tf+v\partial_xf-E\partial_vf=0,\qquad\partial_xE=n_0-\int_{\mathbb{R}}f\,dv,\qquad\int_0^LE\,dx=0.
```

Равновесие: $`f=n_0F_0(v)`$, $`E=0`$, $`F_0(v)=(2\pi\theta)^{-1/2}e^{-v^2/(2\theta)}`$; $`\omega_p=\sqrt{n_0}`$, $`\lambda_D=\sqrt\theta/\omega_p`$. Линеаризуем: $`f=n_0F_0+f_1`$, $`\rho_1=\int f_1dv`$, отбрасывая квадратичный член $`E\partial_vf_1`$.

(а) Пусть $`k\in\frac{2\pi}L\mathbb{Z}`$, $`k>0`$ (при $`k<0`$ всё аналогично, так как $`F_0`$ чётна), $`g(v)=\hat f_1(0,k,v)`$ — гладкая, $`\lvert g(v)\rvert\le Ce^{-\lvert v\rvert}`$. Доказать, что при $`\mathrm{Re}\,p>0`$

```math
\tilde\rho_1(k,p)=\frac{N(k,p)}{\varepsilon(k,p)},\qquad N=\int_{\mathbb{R}}\frac{g(v)\,dv}{p+ikv},\qquad\varepsilon(k,p)=1-\frac{\omega_p^2}{k^2}\int_{\mathbb{R}}\frac{F_0'(v)\,dv}{v-\omega/k},\quad\omega=ip.
```

(б) Доказать, что $`\varepsilon(k,p)\neq0`$ при $`\mathrm{Re}\,p>0`$ (нет растущих мод). Выписать аналитическое продолжение $`\int_{\mathbb{R}}F_0'(v)(v-c)^{-1}dv`$ на $`\mathrm{Im}\,c\le0`$ (правило обхода Ландау) и объяснить на физическом уровне строгости, как асимптотика $`\hat\rho_1(k,t)`$ при $`t\to\infty`$ определяется нулями продолженной $`\varepsilon`$.

(в) Длинноволновый предел $`k\lambda_D\to0`$. Считая $`\lvert\mathrm{Im}\,\omega\rvert\ll\mathrm{Re}\,\omega`$ и разлагая главное значение формально по степеням $`v/c`$, вывести, что корень $`\varepsilon=0`$ имеет вид $`\omega=\omega_r+i\gamma`$ с

```math
\omega_r^2=\omega_p^2\left(1+3k^2\lambda_D^2+O(k^4\lambda_D^4)\right),\qquad\gamma\approx-\sqrt{\frac\pi8}\,\frac{\omega_p}{(k\lambda_D)^3}\exp\left(-\frac{1}{2k^2\lambda_D^2}-\frac32\right).
```

## Часть E. Задачи повышенной сложности (≈ 40 мин, 15 баллов)

Нестандартные задачи: проверяют, умеете ли вы применять теорию там, где путь не подсказан. Не огорчайтесь, если не все решены. E1 — 7 баллов, E2 — 8 баллов.

**E1.** Равновесия неоднородного газа. Пусть $`B>0`$ на $`(0,\infty)\times(-1,1)`$. (а) Пусть $`f\in C^\infty(\mathbb{T}^3\times\mathbb{R}^3)`$ — положительное стационарное решение $`v\cdot\nabla_xf=Q(f,f)`$ с гауссовыми оценками. Доказать, что $`f`$ — глобальный максвеллиан $`M_{\rho,u,\theta}`$ с постоянными $`\rho,u,\theta`$ (результатами D1 можно пользоваться). (б) Пусть теперь $`x\in\mathbb{R}^3`$. Найти все гладкие положительные $`f`$, которые при каждом $`x`$ являются максвеллианами по $`v`$ и удовлетворяют $`v\cdot\nabla_xf=0`$, и доказать, что ни у одной из них масса $`\iint f\,dx\,dv`$ не конечна. Что отсюда следует (формально) для стационарных решений уравнения Больцмана на $`\mathbb{R}^3`$ с конечной массой и быстрым убыванием по $`x`$?

**E2.** Затухание Ландау, которое можно вычислить точно. В условиях D2 заменим максвелловский фон лоренцевым: $`F_0(v)=\frac{a}{\pi(v^2+a^2)}`$, $`a>0`$ (у него бесконечна энергия, но линеаризованная задача имеет смысл). Пусть $`f_1(0,x,v)=\alpha n_0\cos(kx)F_0(v)`$, $`k\in\frac{2\pi}L\mathbb{Z}`$, $`k>0`$. (а) Найти вычетами $`\varepsilon(k,p)`$ и $`N(k,p)`$ при $`\mathrm{Re}\,p>0`$. (б) Найти аналитическое продолжение $`\varepsilon`$ и все его нули. (в) Найти $`\rho_1(t,x)`$ при $`t\ge0`$ точно. (г) Сравнить с решением свободного переноса $`f_1(0,x-vt,v)`$ (без поля) и с ответом D2(в): почему здесь затухание не экспоненциально мало при $`k\to0`$?

## Карта навыков

| Тема из «Содержания» | Задачи |
|---|---|
| Функция распределения, иерархия ББГКИ | A1 |
| Приближения среднего поля (уравнение Власова) и Больцмана–Грэда; теорема Ланфорда | A1, A2 |
| Уравнение Больцмана, интеграл столкновений, инварианты столкновений, H-теорема, максвелловские распределения (контрольная точка) | A3, A4, A5, B1, D1, E1 |
| Гидродинамический предел: уравнения Эйлера и Навье–Стокса по Гильберту и Чепмену–Энскогу, коэффициенты переноса | A9, B3, C1, C3 |
| Линеаризованный оператор Больцмана и модель BGK | A6, A7, B2, C2, C3 |
| Уравнение Власова–Пуассона, линейное затухание Ландау (контрольная точка) | A8, B4, D2, E2 |
| Броуновское движение: уравнения Ланжевена и Фоккера–Планка, соотношение Эйнштейна, флуктуационно-диссипационная теорема | C4, C5 |
| Уравнение Крамерса и гипокоэрцитивность | A10, B5 |

Если по теме потеряно больше половины баллов — к ней стоит вернуться:
- ББГКИ, среднее поле, Больцман–Грэд, Ланфорд — Gallagher, Saint-Raymond, Texier «From Newton to Boltzmann», вводные главы; Golse «On the dynamics of large particle systems in the mean field limit» (лекции, дополнительно к карточке);
- уравнение Больцмана, инварианты, H-теорема — Villani «A review of mathematical topics in collisional kinetic theory», гл. 1; Cercignani «The Boltzmann Equation and Its Applications», главы об интеграле столкновений и H-теореме; Лифшиц, Питаевский «Физическая кинетика», гл. I;
- гидродинамические пределы, коэффициенты переноса — Golse «The Boltzmann equation and its hydrodynamic limits», формальные пределы; Saint-Raymond «Hydrodynamic Limits of the Boltzmann Equation», вводные главы; Лифшиц–Питаевский, гл. I (вязкость и теплопроводность);
- линеаризованный оператор и BGK — Cercignani, главы о линеаризованном уравнении и модельных уравнениях; Villani, гл. 1;
- Власов–Пуассон и затухание Ландау — Лифшиц–Питаевский, гл. III «Бесстолкновительная плазма»; Mouhot, Villani «On Landau damping» (Acta Math. 207, 2011), введение и раздел о линейном затухании;
- Ланжевен, Фоккер–Планк, Эйнштейн — Лифшиц–Питаевский, гл. II «Диффузионное приближение»; Pavliotis «Stochastic Processes and Applications», главы об уравнениях Фоккера–Планка и Ланжевена (дополнительно к карточке);
- Крамерс и гипокоэрцитивность — Villani «Hypocoercivity» (Mem. AMS 202, 2009), часть I.

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
| 0–39 | Не усвоено | Проверить пререквизиты: части A и C диагностик Q9, D3 (перенос, Фурье и Лаплас, энергетические оценки), P3 (марковские и гауссовы процессы), а также R5; затем Лифшиц–Питаевский, гл. I–III, и Villani review, гл. 1 |
| 40–59 | Фрагментарно | По карте навыков выбрать провальные темы; самостоятельно провести вычисления: слабая форма интеграла столкновений, Чепмен–Энског для BGK, дисперсионное соотношение плазмы |
| 60–74 | Рабочий уровень | Можно переходить к связанным дисциплинам — P4 (уравнения Фоккера–Планка и Ланжевена в общей форме) и Q8 (гидродинамические уравнения), — параллельно закрывая пробелы; критически важны H-теорема и затухание Ландау |
| 75–89 | Уверенно | Можно ставить галочку в plan.md |
| 90–100 | Свободное владение | Переходить к исследовательской литературе: Gallagher–Saint-Raymond–Texier (теорема Ланфорда), Saint-Raymond (предел Навье–Стокса), Mouhot–Villani «On Landau damping» (нелинейное затухание), Villani «Hypocoercivity» |

**Правило галочки:** ставить `[x]` напротив Q10 в plan.md, если итог ≥ 75, в каждой из частей A–D набрано не меньше половины баллов, а обе задачи с пометкой «контрольная точка» (D1 и D2) решены полностью.

**Диагностика по профилю:**
- A высокое, C низкое — нет навыка счёта: прорешать моменты максвеллиана, Чепмена–Энскога для BGK и процесс Орнштейна–Уленбека (Лифшиц–Питаевский, гл. I–II).
- Высокие D1, C1–C3 при низких D2, E2, B4 — освоена столкновительная кинетика, но не бесстолкновительная: гл. III Лифшица–Питаевского, введение Mouhot–Villani, фазовое перемешивание для свободного переноса.
- Высокие C4, C5 при низких A10, B5 — броуновское движение усвоено, кинетическая сторона — нет: часть I «Hypocoercivity» Виллани (почему диссипация только по $`v`$ даёт сходимость по $`x`$).
- E = 0 при остальном ≥ 75 — нормально: к равновесиям неоднородного газа и точно решаемым моделям затухания можно вернуться при чтении исследовательской литературы.

## Ключ для самопроверки

<details>
<summary>Открыть только после окончания экзамена</summary>

### Часть A

1. $`f_N(t,z_1,\dots,z_N)`$, $`z_i=(x_i,v_i)`$, — симметричная вероятностная плотность, решение уравнения Лиувилля $`\partial_tf_N+\sum_iv_i\cdot\nabla_{x_i}f_N-\sum_i\sum_{j\neq i}\nabla\Phi(x_i-x_j)\cdot\nabla_{v_i}f_N=0`$; $`f_N^{(s)}=\int f_N\,dz_{s+1}\cdots dz_N`$. Интегрируя по $`z_2,\dots,z_N`$ (слагаемые с $`i\ge2`$ — дивергенции), получаем $`\partial_tf_N^{(1)}+v_1\cdot\nabla_{x_1}f_N^{(1)}=(N-1)\int\nabla\Phi(x_1-x_2)\cdot\nabla_{v_1}f_N^{(2)}dz_2`$. При $`\Phi=\Phi_0/N`$ и $`f_N^{(2)}\approx f\otimes f`$ (хаотичность; её сохранение — распространение хаоса) получается уравнение Власова $`\partial_tf+v\cdot\nabla_xf-(\nabla\Phi_0\ast\rho_f)\cdot\nabla_vf=0`$, $`\rho_f=\int f\,dv`$. Строго — для липшицевой силы $`\nabla\Phi_0`$ (Braun–Hepp, Dobrushin).
2. $`N\to\infty`$, $`\varepsilon\to0`$, $`N\varepsilon^2=\ell^{-1}`$ фиксировано (в размерности $`d`$: $`N\varepsilon^{d-1}`$): частица на пути $`1`$ заметает объём $`\sim\varepsilon^2`$ и встречает $`\sim N\varepsilon^2`$ частиц, так что длина свободного пробега $`\ell\sim1`$, а объёмная доля $`N\varepsilon^3\to0`$. Ланфорд (1975; полностью — Gallagher–Saint-Raymond–Texier, 2013): если $`f_N(0)=Z_N^{-1}f_0^{\otimes N}\mathbf{1}_{\mathcal{D}_N^\varepsilon}`$ (хаос без перекрытий), $`f_0`$ непрерывна, $`0\le f_0\le Ce^{-\beta\lvert v\rvert^2/2}`$, то при $`t\le T^*(C,\beta)`$ (доля времени свободного пробега) $`f_N^{(s)}(t)\to f(t)^{\otimes s}`$ (в смысле наблюдаемых), $`f`$ — решение уравнения Больцмана для твёрдых сфер ($`B=\mathrm{const}\cdot\lvert v-v_*\rvert`$) с данными $`f_0`$. Необратимость возникает в пределе. Критерии: масштаб с объяснением — 1; теорема (хаос, малое время, маргиналы, сечение) — 1.
3. $`v'+v'_*=v+v_*`$ очевидно; $`\lvert v'\rvert^2+\lvert v'_*\rvert^2=2\left\lvert\frac{v+v_*}2\right\rvert^2+2\frac{\lvert v-v_*\rvert^2}4=\lvert v\rvert^2+\lvert v_*\rvert^2`$. Твёрдые сферы: $`B=C\lvert v-v_*\rvert`$; максвелловские молекулы: $`B=b(\cos\theta)`$ (не зависит от $`\lvert v-v_*\rvert`$; для потенциала $`r^{-4}`$). Обрезание Грэда: $`A(\lvert z\rvert)=\int_{S^2}B(\lvert z\rvert,\cos\theta)d\sigma<\infty`$ (локально ограничено); тогда $`Q^+(f,f)=\iint Bf'f'_*`$, $`Q^-(f,f)=f\cdot(A\ast f)`$, $`(A\ast f)(v)=\int A(\lvert v-v_*\rvert)f_*dv_*`$ — частота столкновений. Для степенных потенциалов $`b`$ не интегрируема при $`\theta\to0`$, и разложения нет.
4. $`\varphi`$ — инвариант столкновений, если $`\varphi(v')+\varphi(v'_*)=\varphi(v)+\varphi(v_*)`$ для всех (п. в.) $`v,v_*,\sigma`$. Теорема ($`d\ge2`$; $`\varphi`$ непрерывна или хотя бы локально интегрируема): $`\varphi=a+b\cdot v+c\lvert v\rvert^2`$. Из слабой формы $`\int Q(f,f)\varphi=0`$ для них, откуда $`\partial_t\int\varphi f\,dv+\nabla_x\cdot\int v\varphi f\,dv=0`$ для $`\varphi=1,v_i,\frac12\lvert v\rvert^2`$ (C1).
5. $`H(f)=\iint f\log f\,dx\,dv`$; $`D(f)(t,x)=\frac14\iiint B\left(f'f'_*-ff_*\right)\log\frac{f'f'_*}{ff_*}d\sigma\,dv_*\,dv\ge0`$; для решений на $`\mathbb{T}^3`$ (или на $`\mathbb{R}^3`$ с убыванием) $`\frac{d}{dt}H=-\int D(f)dx\le0`$; $`D(f)(t,x)=0\iff f(t,x,\cdot)`$ — максвеллиан (локальный). Строго: для однородного уравнения с твёрдыми сферами решения с конечными массой, энергией и энтропией существуют, единственны и удовлетворяют H-теореме (Arkeryd; Mischler–Wennberg); для неоднородного ренормализованные решения DiPerna–Lions удовлетворяют лишь неравенству $`H(t)+\int_0^t\int D\le H(0)`$, а классические глобальные решения известны только вблизи равновесия (Ukai, Guo). Критерии: определения и утверждение — 1; статус — 1.
6. $`Lh=\iint B\,M_*\left(h'+h'_*-h-h_*\right)d\sigma\,dv_*`$ (линейная часть $`M^{-1}Q(f,f)`$, так как $`M'M'_*=MM_*`$). В $`L^2(M\,dv)`$: $`\langle Lh,g\rangle=-\frac14\iiint BMM_*\left(h'+h'_*-h-h_*\right)\left(g'+g'_*-g-g_*\right)`$, поэтому $`L`$ симметричен и $`L\le0`$; $`\ker L=\mathrm{span}\lbrace1,v_1,v_2,v_3,\lvert v\rvert^2\rbrace`$ (инварианты столкновений). При обрезании $`L=K-\nu(v)`$, $`\nu(v)=\iint BM_*\,d\sigma\,dv_*`$ — частота столкновений, $`K`$ компактен (Гильберт, Грэд). Для твёрдых сфер $`\nu(v)\asymp1+\lvert v\rvert`$, и есть спектральная щель: $`-\langle Lh,h\rangle\ge\lambda\lVert h-\Pi h\rVert^2`$, $`\Pi`$ — проектор на $`\ker L`$. Критерии: формула, симметрия, знак — 1; ядро и щель — 1.
7. $`\partial_tf+v\cdot\nabla_xf=\tau^{-1}(M[f]-f)`$, $`M[f]=M_{\rho,u,\theta}`$ с полями самой $`f`$ ($`\tau`$ может зависеть от $`\rho,\theta`$). Сохраняет массу, импульс, энергию ($`\int(M[f]-f)\varphi=0`$ для $`\varphi=1,v,\lvert v\rvert^2`$), равновесия — локальные максвеллианы, есть H-теорема (B2). Дефект: все моменты релаксируют со скоростью $`1/\tau`$, поэтому $`\mathrm{Pr}=1`$ (C3), а у одноатомных газов $`\mathrm{Pr}\approx2/3`$ (модель ES-BGK). Критерии: определение — 1; свойства и $`\mathrm{Pr}`$ — 1.
8. $`\partial_tf+v\cdot\nabla_xf+E\cdot\nabla_vf=0`$, $`E=-\nabla_x\phi`$, $`-\Delta\phi=\kappa\rho`$, $`\rho=\int f\,dv`$, то есть $`E(t,x)=\kappa\int\frac{x-y}{4\pi\lvert x-y\rvert^3}\rho(t,y)dy`$; $`\kappa=+1`$ — плазма, $`\kappa=-1`$ — гравитация. Сохраняются масса, импульс, энергия $`\frac12\iint\lvert v\rvert^2f+\frac\kappa2\int\lvert E\rvert^2dx`$ и все $`\iint G(f)`$ (фазовый поток бездивергентен), в частности $`\lVert f\rVert_{L^p}`$ и $`H(f)`$. Теорема (Pfaffelmoser 1992; Schaeffer 1991; Lions–Perthame 1991): при $`0\le f_0\in C^1_c(\mathbb{R}^6)`$ существует единственное глобальное классическое решение (в обоих случаях). Критерии: система и сохранение — 1; теорема — 1.
9. $`\partial_tf+v\cdot\nabla_xf=\varepsilon^{-1}Q(f,f)`$, $`f=\sum_n\varepsilon^nf_n`$ (Гильберт). Порядок $`\varepsilon^{-1}`$: $`Q(f_0,f_0)=0`$, $`f_0=M_{\rho,u,\theta}`$; порядок $`\varepsilon^0`$: $`(\partial_t+v\cdot\nabla_x)f_0=Q(f_0,f_1)+Q(f_1,f_0)`$, условие разрешимости (ортогональность ядру линеаризованного оператора) — уравнения Эйлера; следующий порядок (Чепмен–Энског) — Навье–Стокс с вязкостью $`O(\varepsilon)`$. Несжимаемый масштаб: $`\varepsilon\partial_tf+v\cdot\nabla_xf=\varepsilon^{-1}Q(f,f)`$, $`f=M(1+\varepsilon g)`$, предел $`g=u\cdot v+\theta\frac{\lvert v\rvert^2-5}2`$, $`(u,\theta)`$ решают несжимаемые уравнения Навье–Стокса–Фурье (Bardos–Golse–Levermore). Строго: Caflisch (1980) — компрессибельный Эйлер на времени жизни гладкого решения; Golse–Saint-Raymond (2004) — ренормализованные решения сходятся к решениям Лерэ. Критерии: Гильберт — 1; несжимаемый масштаб и результаты — 1.
10. $`\partial_tf+v\cdot\nabla_xf-\nabla V\cdot\nabla_vf=\nabla_v\cdot(\nabla_vf+vf)`$, равновесие $`\mu=Z^{-1}e^{-V(x)-\lvert v\rvert^2/2}`$. Для $`h=f/\mu`$: $`\partial_th+\mathcal{L}h=0`$, $`\mathcal{L}=A^{\ast}A+B`$ в $`L^2(\mu)`$, $`A=\nabla_v`$, $`B=v\cdot\nabla_x-\nabla V\cdot\nabla_v`$ антисимметричен. $`\mathcal{L}`$ гипокоэрцитивен в гильбертовом $`\tilde H`$ (например, $`H^1(\mu)`$), если $`\lVert e^{-t\mathcal{L}}h\rVert_{\tilde H}\le Ce^{-\lambda t}\lVert h\rVert_{\tilde H}`$ при $`h\perp\ker\mathcal{L}`$ с $`C\ge1`$, $`\lambda>0`$ ($`C>1`$ существенно: норма не убывает монотонно). Не коэрцитивен: $`\langle\mathcal{L}h,h\rangle=\lVert\nabla_vh\rVert^2=0`$ на функциях от $`x`$. Чинит коммутатор $`[A,B]=\nabla_x`$ (Хёрмандер); теорема Виллани: при условиях на $`V`$ (например, $`\nabla^2V`$ ограничен, $`e^{-V}dx`$ удовлетворяет неравенству Пуанкаре) есть гипокоэрцитивность в $`H^1(\mu)`$. Критерии: уравнение и равновесие — 1; определение и некоэрцитивность — 1.

### Часть B

1. **Неверно.** При $`d=1`$: $`k=\pm1`$, $`\sigma=k`$ даёт $`v'=v`$, $`v'_*=v_*`$, а $`\sigma=-k`$ даёт $`v'=v_*`$, $`v'_*=v`$. В обоих случаях $`f'f'_*=ff_*`$, поэтому $`Q(f,f)\equiv0`$ для любой $`f`$, например $`f=(2+\cos v)e^{-v^2}`$ (гауссовы оценки выполнены: $`e^{-v^2}\le f\le3e^{-v^2}`$, но $`\log f`$ — не квадратичный многочлен). Всякая функция — инвариант столкновений; в D1(г) существенно $`d\ge2`$.
2. **Верно.** $`\frac{d}{dt}H=\iint(1+\log f)\partial_tf=-\iint(1+\log f)v\cdot\nabla_xf+\tau^{-1}\iint(1+\log f)(M-f)`$. Первое слагаемое $`=-\iint v\cdot\nabla_x(f\log f)=0`$ (периодичность), $`\iint(M-f)=0`$. Далее $`\int(M-f)\log f\,dv=\int(M-f)\log\frac fM\,dv+\int(M-f)\log M\,dv`$; второй интеграл равен $`0`$, так как $`\log M=a+b\cdot v+c\lvert v\rvert^2`$, а моменты $`1,v,\lvert v\rvert^2`$ у $`M`$ и $`f`$ совпадают; первый $`\le0`$, так как $`(M-f)(\log f-\log M)\le0`$ поточечно (монотонность логарифма). Итого $`\frac{d}{dt}H\le0`$.
3. **Неверно.** Так как $`Q(M,M)=0`$, локальный максвеллиан — решение тогда и только тогда, когда $`(\partial_t+v\cdot\nabla_x)M=0`$, а это гораздо сильнее уравнений Эйлера (те — лишь моменты этого тождества). Контрпример: $`u=0`$, $`\theta(x)=1+\frac12\sin x_1`$, $`\rho=1/\theta`$ — стационарное решение Эйлера ($`p\equiv1`$, $`\nabla p=0`$, $`\nabla\cdot(\rho u)=0`$). Но $`\partial_tM=0`$, а $`\nabla_x\log M=-\frac52\frac{\nabla\theta}\theta+\frac{\lvert v\rvert^2}{2\theta^2}\nabla\theta\not\equiv0`$, так что $`v\cdot\nabla_xM\neq0`$.
4. **Верно.** $`\hat\rho_k(t)=\int\hat f_0(k,v)e^{-ikvt}dv=\Psi(k,kt)`$, где $`\Psi(k,\eta)=\iint f_0(x,v)e^{-ikx-i\eta v}dx\,dv`$ и $`\lvert\Psi(k,\eta)\rvert\le C_n(1+\lvert k\rvert+\lvert\eta\rvert)^{-n-2}`$ (интегрирование по частям, $`f_0\in C_c^\infty`$). Тогда $`\sup_x\lvert\rho-\bar\rho\rvert\le\frac1{2\pi}\sum_{k\neq0}\lvert\Psi(k,kt)\rvert\le C_nt^{-n}`$ при $`t\ge1`$. Не экспоненциально: $`f_0=(1+\cos x)g(v)`$, $`0\le g\in C_c^\infty`$, $`g\not\equiv0`$; тогда $`\rho(t,x)-\bar\rho=\mathrm{Re}\left(e^{ix}\hat g(t)\right)`$, и $`\sup_x\lvert\rho-\bar\rho\rvert=\lvert\hat g(t)\rvert`$. Если $`\lvert\hat g(t)\rvert\le Ce^{-a\lvert t\rvert}`$ (при $`t<0`$ — так как $`\hat g(-t)=\overline{\hat g(t)}`$), то $`g=\frac1{2\pi}\int\hat g(t)e^{ivt}dt`$ голоморфна в полосе $`\lvert\mathrm{Im}\,v\rvert < a`$, а аналитическая функция с компактным носителем — нуль. (Поэтому у Муо–Виллани нужна аналитичность или Жевре.)
5. **Неверно.** Транспортная часть антисимметрична: $`\int v\partial_xh\cdot h\,d\mu=\int v\partial_x\frac{h^2}2d\mu=0`$, а $`\int(\partial_v^2h-v\partial_vh)h\,d\mu=-\int(\partial_vh)^2d\mu`$. Значит, $`\langle-Lh,h\rangle=\lVert\partial_vh\rVert^2`$, и при $`h=\cos x`$ левая часть $`0`$, а $`\lVert h-\int h\,d\mu\rVert^2=\frac12`$. Тем не менее решения сходятся к $`\int h_0d\mu`$ экспоненциально — гипокоэрцитивность (A10).

### Часть C

**C1.** (а) Умножая уравнение на $`\varphi`$ и интегрируя по $`v`$: $`\partial_t\int\varphi f+\nabla_x\cdot\int v\varphi f=\int Q\varphi=0`$. Подставляя $`v=u+w`$, $`\int wf=0`$:

<div align="center">

$`\displaystyle \partial_t\rho+\nabla\cdot(\rho u)=0,\quad\partial_t(\rho u)+\nabla\cdot(\rho u\otimes u+P)=0,\quad\partial_t\left(\frac{\rho\lvert u\rvert^2}2+\frac{3\rho\theta}2\right)+\nabla\cdot\left(\rho u\left(\frac{\lvert u\rvert^2}2+\frac{3\theta}2\right)+Pu+q\right)=0.`$

</div>

(Здесь $`\int\frac{\lvert v\rvert^2}2f=\frac{\rho\lvert u\rvert^2}2+\frac{3\rho\theta}2`$, $`\int v\frac{\lvert v\rvert^2}2f=\rho u\left(\frac{\lvert u\rvert^2}2+\frac{3\theta}2\right)+Pu+q`$.) (б) Для максвеллиана $`w\sim N(0,\theta I)`$ (с весом $`\rho`$): $`P=\rho\theta I`$, $`q=0`$ (нечётный момент). (в) С $`p=\rho\theta`$, $`\mathcal{E}=\frac{\rho\lvert u\rvert^2}2+\frac32p`$: $`\partial_t\rho+\nabla\cdot(\rho u)=0`$, $`\partial_t(\rho u)+\nabla\cdot(\rho u\otimes u)+\nabla p=0`$, $`\partial_t\mathcal{E}+\nabla\cdot\left((\mathcal{E}+p)u\right)=0`$; $`\rho e=\frac32p=\frac{p}{\gamma-1}`$, $`\gamma=\frac53`$. Линеаризация: $`\partial_t\tilde\rho+\rho_0\nabla\cdot\tilde u=0`$, $`\rho_0\partial_t\tilde u+\nabla\tilde p=0`$, $`\frac32\partial_t\tilde p+\frac52p_0\nabla\cdot\tilde u=0`$, откуда $`\partial_t^2\tilde p=\frac53\frac{p_0}{\rho_0}\Delta\tilde p`$, $`c^2=\frac53\theta_0`$. Критерии: (а) — 2; (б) — 2; (в) — 2.

**C2.** (а) $`V=\frac{v+v_*}2`$, $`w=v-v_*`$: $`\varphi(v)+\varphi(v_*)=2V^{\mathsf T}AV+\frac12w^{\mathsf T}Aw`$, $`\varphi'+\varphi'_*=2V^{\mathsf T}AV+\frac12\lvert w\rvert^2\sigma^{\mathsf T}A\sigma`$; разность — требуемая. (б) $`\sigma=\cos\theta\,k+\sin\theta\,\omega`$, $`\omega\perp k`$; среднее по окружности $`\omega`$: $`\langle\omega\omega^{\mathsf T}\rangle=\frac12(I-kk^{\mathsf T})`$, перекрёстный член исчезает. Так как $`\mathrm{tr}\,A=0`$, $`\langle\sigma^{\mathsf T}A\sigma\rangle=\cos^2\theta\,k^{\mathsf T}Ak-\frac12\sin^2\theta\,k^{\mathsf T}Ak`$, и $`\langle\sigma^{\mathsf T}A\sigma\rangle-k^{\mathsf T}Ak=-\frac32\sin^2\theta\,k^{\mathsf T}Ak`$; интегрируя с весом $`b(\cos\theta)`$, получаем $`-\frac32\Lambda k^{\mathsf T}Ak`$. (в) $`\int Q\varphi=\frac12\iint ff_*\cdot\frac12\lvert w\rvert^2\left(-\frac32\Lambda k^{\mathsf T}Ak\right)=-\frac38\Lambda\iint ff_*(v-v_*)^{\mathsf T}A(v-v_*)=-\frac34\rho\Lambda\int f\varphi`$ (использовано $`\int vf=0`$). Так как $`\int f\varphi=\mathrm{tr}(\Pi A)`$ для всех бесследовых $`A`$, $`\dot\Pi=-\lambda\Pi`$, $`\lambda=\frac34\rho\Lambda`$ (для $`b\equiv\frac1{4\pi}`$: $`\lambda=\frac\rho2`$). В однородной BGK $`M[f]`$ не зависит от $`t`$ (моменты сохраняются), $`f(t)=e^{-t/\tau}f_0+(1-e^{-t/\tau})M`$, $`\Pi(t)=e^{-t/\tau}\Pi(0)`$; совпадение при $`\tau=\frac{4}{3\rho\Lambda}`$. (Поток тепла у максвелловских молекул релаксирует со скоростью $`\frac23\lambda`$, отсюда их $`\mathrm{Pr}=\frac23`$, а у BGK — $`1`$.) Критерии: (а) — 1; (б) — 2; (в) — 3 ($`\lambda`$ — 2, BGK — 1).

**C3.** (а) $`\int f^{(1)}\varphi=-\left(\partial_t\int M\varphi+\nabla_x\cdot\int vM\varphi\right)`$ — это в точности левые части уравнений Эйлера (C1 с $`P=\rho\theta I`$, $`q=0`$), которые равны нулю, так как $`\partial_t`$ вычислены по ним. (б) По Эйлеру $`\partial_t\rho=-\partial_1(\rho U)=0`$, $`\partial_tu=-U\partial_1u-\nabla p/\rho=0`$, $`\partial_t\theta=-u\cdot\nabla\theta-\frac23\theta\nabla\cdot u=0`$. Поэтому $`f^{(1)}=-v_2\partial_2M=-\frac{U'}\theta v_2(v_1-U)M`$ и $`P_{12}=\tau\int(v_1-U)v_2f^{(1)}dv=-\tau\frac{U'}\theta\int(v_1-U)^2v_2^2M\,dv=-\rho\theta\tau\,U'`$. (в) $`u=0`$, $`\nabla p=0`$: все $`\partial_t=0`$. $`\log M=\log p-\frac52\log\theta-\frac{\lvert v\rvert^2}{2\theta}+\mathrm{const}`$, $`f^{(1)}=-v_2\theta'\partial_\theta M=-\frac{\theta'}\theta v_2\left(\frac{\lvert v\rvert^2}{2\theta}-\frac52\right)M`$. С $`\int v_2^2\lvert v\rvert^4M=35\rho\theta^3`$, $`\int v_2^2\lvert v\rvert^2M=5\rho\theta^2`$: $`q_2=\tau\int v_2\frac{\lvert v\rvert^2}2f^{(1)}dv=-\tau\frac{\theta'}\theta\rho\left(\frac{35}4-\frac{25}4\right)\theta^2=-\frac52\rho\theta\tau\,\theta'`$, $`\kappa=\frac52\rho\theta\tau`$, $`\mathrm{Pr}=1`$. Порядок величины: $`\tau`$ — время свободного пробега, $`\ell\sim\sqrt\theta\,\tau`$, и $`\mu/\rho=\theta\tau\sim\ell\sqrt\theta`$. Критерии: (а) — 2; (б) — 2; (в) — 2.

**C4.** (а) $`\partial_tp=\nabla\cdot\left(p\nabla\log\frac p\gamma\right)`$ (так как $`\nabla p+p\nabla V=p\nabla\log\frac p\gamma`$). Тогда $`\frac{d}{dt}\int p\log\frac p\gamma=\int\partial_tp\left(\log\frac p\gamma+1\right)=-\int p\left\lvert\nabla\log\frac p\gamma\right\rvert^2`$. Для стационарной $`p`$ правая часть $`0`$, $`p/\gamma`$ постоянна, а нормировка даёт $`p=\gamma`$. (б) $`\partial_th=\Delta h-\nabla V\cdot\nabla h`$ (оператор $`\mathcal{G}h=\gamma^{-1}\nabla\cdot(\gamma\nabla h)`$ симметричен в $`L^2(\gamma)`$); $`\int h\gamma=1`$ сохраняется, $`\frac{d}{dt}\int(h-1)^2\gamma=2\int(h-1)\nabla\cdot(\gamma\nabla h)=-2\int\lvert\nabla h\rvert^2\gamma\le-\frac2{C_P}\lVert h-1\rVert^2`$, откуда $`\lVert h_t-1\rVert\le e^{-t/C_P}\lVert h_0-1\rVert`$. (в) Многочлены Эрмита $`He_n`$: $`He_n'=nHe_{n-1}`$, $`\lVert He_n\rVert^2_{L^2(\gamma)}=n!`$, $`e_n=He_n/\sqrt{n!}`$ — ортонормированный базис. Для $`g=\sum c_ne_n`$: $`g'=\sum_{n\ge1}c_n\sqrt n\,e_{n-1}`$ (коэффициенты $`g'`$ находятся интегрированием по частям: $`\int g'He_{n-1}d\gamma=\int g\,He_n\,d\gamma`$), так что $`\int g'^2d\gamma=\sum_{n\ge1}nc_n^2\ge\sum_{n\ge1}c_n^2=\mathrm{Var}_\gamma(g)`$. Неулучшаемость: $`h_0=1+\epsilon x`$ даёт $`h_t=1+\epsilon e^{-t}x`$ ($`\partial_th=h''-xh'`$). (Если требовать $`p>0`$: для $`h_0=e^{\epsilon x-\epsilon^2/2}`$ коэффициент при $`e_1`$ равен $`\epsilon\neq0`$, и $`\lVert h_t-1\rVert^2=\sum_{n\ge1}c_n^2e^{-2nt}\ge\epsilon^2e^{-2t}`$.) Критерии: (а) — 2; (б) — 2; (в) — 2.

**C5.** (а) $`v_t=e^{-\gamma t}v_0+\sqrt{2\gamma\theta/m}\int_0^te^{-\gamma(t-s)}dW_s`$, закон $`N\left(e^{-\gamma t}v_0,\frac\theta m(1-e^{-2\gamma t})\right)\to N(0,\theta/m)`$. Уравнение Фоккера–Планка: $`\partial_tp=\gamma\partial_v(vp)+\frac{\gamma\theta}m\partial_v^2p=\gamma\partial_v\left(vp+\frac\theta m\partial_vp\right)`$; для $`p\propto e^{-mv^2/(2\theta)}`$ скобка равна $`0`$. (б) Процесс стационарен: $`\mathbb{E}\,v_sv_t=\frac\theta me^{-\gamma\lvert t-s\rvert}`$. $`\mathbb{E}(x_t-x_0)^2=\int_0^t\int_0^t\mathbb{E}\,v_sv_r\,ds\,dr=2\int_0^t(t-s)\frac\theta me^{-\gamma s}ds=\frac{2\theta}{m\gamma}\left(t-\frac{1-e^{-\gamma t}}\gamma\right)`$; при $`t\to\infty`$ это $`2Dt+O(1)`$, $`D=\frac\theta{m\gamma}`$; при $`t\to0`$ — $`\frac\theta mt^2`$ (баллистический режим). (в) $`\mathbb{E}\,v_t\to\frac{F}{m\gamma}`$, подвижность $`\frac1{m\gamma}`$, и $`D=\theta\cdot\frac1{m\gamma}`$; $`\int_0^\infty\frac\theta me^{-\gamma t}dt=\frac\theta{m\gamma}=D`$. ФДТ: шум $`\sigma^2=\frac{2\gamma\theta}m`$ однозначно определяется трением и температурой (иначе стационарная мера — не $`N(0,\theta/m)`$); эквивалентно — отклик на силу выражается через равновесные флуктуации (Грин–Кубо). Критерии: (а) — 2; (б) — 2; (в) — 2.

### Часть D

**D1.** Схема.
1. (а) Обмен $`v\leftrightarrow v_*`$ вместе с $`\sigma\mapsto-\sigma`$ (сохраняет меру) переставляет $`v'\leftrightarrow v'_*`$ и не меняет $`\cos\theta=k\cdot\sigma`$ ($`k\mapsto-k`$), поэтому $`\int Q\varphi=\frac12\iiint B(f'f'_*-ff_*)(\varphi+\varphi_*)`$. Для $`T\colon(v,v_*,\sigma)\mapsto(v',v'_*,k)`$: $`\lvert v'-v'_*\rvert=\lvert v-v_*\rvert`$, новое направление относительной скорости $`k'=\sigma`$, новый параметр $`\sigma'=k`$, так что $`\cos\theta'=\sigma\cdot k=\cos\theta`$ и $`B`$ инвариантно; $`T`$ переставляет $`(v,v_*)`$ и $`(v',v'_*)`$. Замена $`T`$ даёт $`\int Q\varphi=-\frac12\iiint B(f'f'_*-ff_*)(\varphi'+\varphi'_*)`$. Среднее двух выражений — требуемая формула.
2. (б) $`\frac{d}{dt}\int f\log f=\int Q(f,f)(1+\log f)=\int Q(f,f)\log f`$ ($`\varphi=1`$ — инвариант). По (а) с $`\varphi=\log f`$ ($`\lvert\log f\rvert\le C(1+\lvert v\rvert^2)`$ по гауссовым оценкам):

<div align="center">

$`\displaystyle \frac{d}{dt}\int f\log f\,dv=-D(f),\qquad D(f)=\frac14\iiint B\left(f'f'_*-ff_*\right)\log\frac{f'f'_*}{ff_*}\,d\sigma\,dv_*\,dv\ge0,`$

</div>

так как $`(X-Y)(\log X-\log Y)\ge0`$ при $`X,Y>0`$, с равенством только при $`X=Y`$. На $`\mathbb{T}^3\times\mathbb{R}^3`$ добавляется $`-\iint v\cdot\nabla_x(f\log f)=0`$, и $`\frac{d}{dt}H=-\int D(f)(x)dx`$.
3. (в) Если $`Q=0`$, то $`D=-\int Q\log f=0`$. Если $`D=0`$, то подынтегральное выражение (неотрицательное, непрерывное) равно $`0`$ при $`B>0`$, то есть для всех $`v\neq v_*`$ и $`\cos\theta\in(-1,1)`$, а по непрерывности — всюду: $`f'f'_*=ff_*`$, что равносильно инвариантности $`\log f`$. Обратно, если $`f'f'_*=ff_*`$, то подынтегральная функция $`Q`$ равна нулю.
4. (г) При $`V=\frac{v+v_*}2`$, $`r=\frac{\lvert v-v_*\rvert}2`$ функция $`\sigma\mapsto\varphi(V+r\sigma)+\varphi(V-r\sigma)`$ постоянна на $`S^2`$; дифференцируя вдоль касательного вектора $`\tau\perp\sigma`$: $`\left(\nabla\varphi(V+r\sigma)-\nabla\varphi(V-r\sigma)\right)\cdot\tau=0`$. Значит, $`F=\nabla\varphi`$ удовлетворяет $`F(v)-F(w)=\lambda(v,w)(v-w)`$ при всех $`v\neq w`$. Положим $`\lambda(v)=\lambda(v,0)`$. Для линейно независимых $`v,w`$: $`\lambda(v)v-\lambda(w)w=\lambda(v,w)(v-w)`$ даёт $`\lambda(v)=\lambda(v,w)=\lambda(w)`$; для зависимых $`v,w\neq0`$ берём третий вектор $`u`$, независимый с ними (здесь нужно $`d\ge2`$). Итак, $`\lambda\equiv2c`$, $`\nabla\varphi(v)=b+2cv`$, $`\varphi=a+b\cdot v+c\lvert v\rvert^2`$. Применяя к $`\varphi=\log f`$: $`f=e^{a+b\cdot v+c\lvert v\rvert^2}`$, интегрируемость даёт $`c<0`$, и $`f=M_{\rho,u,\theta}`$ с $`\theta=-\frac1{2c}`$, $`u=-\frac{b}{2c}`$, $`\rho=e^{a-c\lvert u\rvert^2}\left(\frac\pi{-c}\right)^{3/2}`$. Обратно, для максвеллиана $`\log M`$ — инвариант, и $`Q(M,M)=0`$ по (в).

Критерии: (а) — 3 (симметрия $`v\leftrightarrow v_*`$ — 1; замена $`T`$ с проверкой инвариантности $`B`$ — 1; итог — 1); (б) — 2; (в) — 2; (г) — 3 (параллельность $`\nabla\varphi(v)-\nabla\varphi(w)`$ и $`v-w`$ — 1; постоянство $`\lambda`$ с использованием $`d\ge2`$ — 1; интегрирование и отождествление с максвеллианом, $`c<0`$ — 1). Для засчитывания КТ нужны (а)–(г) полностью; в (б) рассуждение для тора можно опустить.

**D2.** Схема.
1. (а) Линеаризация: $`\partial_tf_1+v\partial_xf_1-n_0EF_0'=0`$, $`\partial_xE=-\rho_1`$. Фурье: $`ik\hat E=-\hat\rho_1`$, $`\hat E=\frac{i}{k}\hat\rho_1`$, и $`\partial_t\hat f_1+ikv\hat f_1=\frac{i\omega_p^2}kF_0'\hat\rho_1`$. Лаплас ($`\mathrm{Re}\,p>0`$): $`(p+ikv)\tilde f_1=g+\frac{i\omega_p^2}kF_0'\tilde\rho_1`$. Делим на $`p+ikv\neq0`$ и интегрируем по $`v`$:

<div align="center">

$`\displaystyle \tilde\rho_1\left(1-\frac{i\omega_p^2}k\int\frac{F_0'\,dv}{p+ikv}\right)=\int\frac{g\,dv}{p+ikv}.`$

</div>

При $`p=-i\omega`$: $`p+ikv=ik(v-\omega/k)`$, и $`\frac{i\omega_p^2}k\cdot\frac1{ik}=\frac{\omega_p^2}{k^2}`$ — получаем $`\varepsilon`$. (Проверка знака: при $`F_0=\delta`$ получилось бы $`\varepsilon=1-\omega_p^2/\omega^2`$, плазменные колебания.)
2. (б) $`c=\omega/k=ip/k`$, $`\mathrm{Im}\,c=\mathrm{Re}\,p/k>0`$. Если $`\varepsilon=0`$, то $`I=\int\frac{F_0'(v)dv}{v-c}=\frac{k^2}{\omega_p^2}>0`$. Но $`F_0'=-\frac v\theta F_0`$ и $`\frac1{v-c}=\frac{v-\bar c}{\lvert v-c\rvert^2}`$: $`\mathrm{Im}\,I=-\frac{\mathrm{Im}\,c}\theta\int\frac{vF_0}{\lvert v-c\rvert^2}=0`$ даёт $`\int\frac{vF_0}{\lvert v-c\rvert^2}=0`$, и тогда $`\mathrm{Re}\,I=-\frac1\theta\int\frac{v(v-\mathrm{Re}\,c)F_0}{\lvert v-c\rvert^2}=-\frac1\theta\int\frac{v^2F_0}{\lvert v-c\rvert^2} < 0`$ — противоречие. Продолжение до целой функции: $`\int_{\mathbb{R}}\frac{F_0'(v)dv}{v-c}+2\pi iF_0'(c)`$ при $`\mathrm{Im}\,c<0`$ и $`\mathrm{v.p.}\int\frac{F_0'(v)dv}{v-c}+i\pi F_0'(c)`$ при $`c\in\mathbb{R}`$ (контур по $`v`$ проходит под полюсом). В $`\hat\rho_1(k,t)=\frac1{2\pi i}\int_{\mathrm{Re}\,p=\beta}e^{pt}\frac{N}{\varepsilon}dp`$ сдвигаем контур влево (для аналитичных данных $`N`$ тоже продолжается) и получаем вычеты в нулях продолженной $`\varepsilon`$; асимптотику даёт ближайший к мнимой оси нуль $`p_1`$, $`\mathrm{Re}\,p_1<0`$ — затухание без диссипации.
3. (в) При $`c\gg\sqrt\theta`$, интегрируя по частям: $`\mathrm{v.p.}\int\frac{F_0'}{v-c}=\int\frac{F_0}{(v-c)^2}\approx\frac1{c^2}\int F_0\left(1+\frac{2v}c+\frac{3v^2}{c^2}+\dots\right)=\frac1{c^2}\left(1+\frac{3\theta}{c^2}+\dots\right)`$ (формально; вклад окрестности $`v\approx c`$ экспоненциально мал). Поэтому $`\varepsilon_r(\omega)=1-\frac{\omega_p^2}{\omega^2}-\frac{3k^2\theta\omega_p^2}{\omega^4}+\dots`$, и $`\varepsilon_r=0`$ даёт $`\omega_r^2=\omega_p^2(1+3k^2\lambda_D^2+\dots)`$ (так как $`k^2\theta/\omega_p^2=k^2\lambda_D^2`$). Мнимая часть по правилу Ландау: $`\varepsilon_i(\omega_r)=-\pi\frac{\omega_p^2}{k^2}F_0'(\omega_r/k)`$. Из $`\varepsilon(\omega_r+i\gamma)\approx\varepsilon_r(\omega_r)+i\gamma\partial_\omega\varepsilon_r+i\varepsilon_i=0`$ и $`\partial_\omega\varepsilon_r\approx\frac{2\omega_p^2}{\omega_r^3}\approx\frac2{\omega_p}`$:

<div align="center">

$`\displaystyle \gamma=-\frac{\varepsilon_i}{\partial_\omega\varepsilon_r}\approx\frac{\pi\omega_p^3}{2k^2}F_0'\left(\frac{\omega_r}k\right)=-\frac{\pi\omega_p^3}{2k^2}\cdot\frac{\omega_p}{k\sqrt{2\pi}\,\theta^{3/2}}e^{-\omega_r^2/(2k^2\theta)}=-\sqrt{\frac\pi8}\,\frac{\omega_p}{(k\lambda_D)^3}e^{-\omega_r^2/(2k^2\theta)}.`$

</div>

В показателе нужна поправка к $`\omega_r`$: $`\frac{\omega_r^2}{2k^2\theta}=\frac{1+3k^2\lambda_D^2+O(k^4\lambda_D^4)}{2k^2\lambda_D^2}=\frac1{2k^2\lambda_D^2}+\frac32+O(k^2\lambda_D^2)`$ — отсюда множитель $`e^{-3/2}`$ (в предэкспоненте $`\omega_r\approx\omega_p`$). Численно (точный корень через функцию Фаддеевой): при $`k\lambda_D=0{,}1`$ и $`0{,}05`$ отношение $`\mathrm{Im}\,\omega`$ к формуле равно $`0{,}969`$ и $`0{,}992`$.

Критерии: (а) — 3; (б) — 3 (отсутствие нулей при $`\mathrm{Re}\,p>0`$ — 2; формула продолжения и роль нулей — 1); (в) — 4 ($`\omega_r`$ — 1; $`\varepsilon_i`$ с правильным знаком по правилу Ландау — 1; формула для $`\gamma`$ — 1; показатель с $`-\frac32`$ — 1). Для засчитывания КТ нужны (а), формула продолжения из (б) и (в) полностью.

### Часть E

**E1.** (а) Умножим уравнение на $`1+\log f`$ и проинтегрируем по $`\mathbb{T}^3\times\mathbb{R}^3`$: слева $`\iint v\cdot\nabla_x(f\log f)=0`$, справа $`\iint Q(f,f)\log f=-\int D(f)(x)dx`$. Значит, $`D(f)(x)\equiv0`$ (неотрицательна и непрерывна), и по D1 при каждом $`x`$: $`\log f=a(x)+b(x)\cdot v+c(x)\lvert v\rvert^2`$, $`c<0`$, с гладкими $`a,b,c`$ (их можно выразить через значения $`\log f`$ в нескольких точках $`v`$). Тогда $`Q=0`$ и $`v\cdot\nabla_x\log f=v\cdot\nabla a+\sum_{i,j}v_iv_j\partial_ib_j+\lvert v\rvert^2v\cdot\nabla c=0`$ для всех $`v`$; однородные части степеней $`1,2,3`$ обращаются в нуль: $`\nabla a=0`$, $`\nabla c=0`$, $`\partial_ib_j+\partial_jb_i=0`$ (уравнение Киллинга). Для $`T_{kij}=\partial_k\partial_ib_j`$ (симметрично по $`k,i`$, антисимметрично по $`i,j`$): $`T_{kij}=-T_{kji}=-T_{jki}=T_{jik}=T_{ijk}=-T_{ikj}=-T_{kij}`$, поэтому $`\nabla^2b=0`$, $`b=b_0+Wx`$ с антисимметричной $`W`$; периодичность даёт $`W=0`$. Итак, $`a,b,c`$ постоянны — глобальный максвеллиан. (б) То же вычисление на $`\mathbb{R}^3`$: $`f=\exp\left(a+(b_0+Wx)\cdot v+c\lvert v\rvert^2\right)`$, $`W^{\mathsf T}=-W`$, $`c<0`$ (вращающиеся максвеллианы). Масса: $`\int f\,dv=e^a\left(\frac\pi{\lvert c\rvert}\right)^{3/2}\exp\left(\frac{\lvert b_0+Wx\rvert^2}{4\lvert c\rvert}\right)\ge e^a\left(\frac\pi{\lvert c\rvert}\right)^{3/2}`$, и интеграл по $`x\in\mathbb{R}^3`$ расходится. Следствие: при быстром убывании по $`x`$ рассуждение (а) проходит и на $`\mathbb{R}^3`$ и даёт одну из найденных функций; значит, таких стационарных решений с конечной массой нет — газ в пустом пространстве разлетается. Критерии: (а) — 4 (энтропийный аргумент — 2; полиномиальное тождество, Киллинг, периодичность — 2); (б) — 3 (вид решений — 2; бесконечная масса и вывод — 1).

**E2.** (а) Пусть $`c=\omega/k=ip/k`$, $`\mathrm{Im}\,c>0`$. Замыкая контур в нижней полуплоскости (единственный полюс там — $`v=-ia`$):

<div align="center">

$`\displaystyle \int\frac{F_0(v)dv}{v-c}=-\frac1{c+ia},\qquad\int\frac{F_0'(v)dv}{v-c}=\int\frac{F_0(v)dv}{(v-c)^2}=\frac1{(c+ia)^2}.`$

</div>

Значит, $`\varepsilon=1-\frac{\omega_p^2}{(\omega+ika)^2}=1+\frac{\omega_p^2}{(p+ka)^2}`$ и, так как $`g=\hat f_1(0,k,\cdot)=\frac{\alpha n_0L}2F_0`$, $`N=\frac{\alpha n_0L}2\cdot\frac1{ik}\int\frac{F_0dv}{v-c}=\frac{\alpha n_0L}2\cdot\frac1{p+ka}`$. (б) Формулы задают мероморфное продолжение на всю плоскость; нули $`\varepsilon`$: $`p+ka=\pm i\omega_p`$, то есть $`p=-ka\pm i\omega_p`$ ($`\omega=\pm\omega_p-ika`$). Обе лежат в $`\mathrm{Re}\,p<0`$. (в) $`\tilde\rho_1=\frac{\alpha n_0L}2\cdot\frac{p+ka}{(p+ka)^2+\omega_p^2}`$, обращение Лапласа: $`\hat\rho_1(k,t)=\frac{\alpha n_0L}2e^{-kat}\cos\omega_pt`$; то же для моды $`-k`$, итого

<div align="center">

$`\displaystyle \rho_1(t,x)=\alpha n_0\,e^{-kat}\cos(\omega_pt)\cos(kx),\qquad t\ge0.`$

</div>

(г) Без поля $`\int F_0(v)\cos(k(x-vt))dv=e^{-kat}\cos kx`$ (характеристическая функция Коши) — то же затухание; поле лишь добавляет колебания с частотой ровно $`\omega_p`$. В D2(в) затухание пропорционально $`F_0'(\omega/k)`$ — доле «резонансных» частиц со скоростью около фазовой $`\omega/k\gg\sqrt\theta`$: у гауссова фона она экспоненциально мала, у лоренцева хвост степенной. Критерии: (а) — 3; (б) — 2; (в) — 2; (г) — 1.

</details>
