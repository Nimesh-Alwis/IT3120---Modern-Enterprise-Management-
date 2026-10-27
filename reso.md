## 3. ES / EF / LS / LF

මේවා Activity එකක් පටන් ගන්න සහ ඉවර කරන්න පුළුවන් කාලයන්.

- **ES – Early Start:** Activity එක පටන් ගන්න පුළුවන් මුල්ම වෙලාව.
- **EF – Early Finish:** Activity එක ඉවර කරන්න පුළුවන් මුල්ම වෙලාව.
- **LS – Late Start:** Project එක Late නොකර Activity එක පටන් ගන්න පුළුවන් අවසාන වෙලාව.
- **LF – Late Finish:** Project එක Late නොකර Activity එක ඉවර කරන්න පුළුවන් අවසාන වෙලාව.

## 4. Earned Value Management (EVM)

**Earned Value Management (EVM)** කියන්නේ Project එකේ Schedule Performance සහ Cost Performance මැනීමට භාවිතා කරන ක්‍රමයකි.

### Key Components

- **Planned Value (PV):** සැලසුම් කර ඇති වැඩ සඳහා වෙන් කළ Budgeted Value එක.
- **Earned Value (EV):** මේ වන විට සම්පූර්ණ කර ඇති වැඩවල Value එක.
- **Actual Cost (AC):** සම්පූර්ණ කර ඇති වැඩ සඳහා සැබෑවටම වැය වූ මුදල.

### Important EVM Metrics

#### 1. Schedule Variance (SV)

Project එකේ වැඩ Schedule එකට සාපේක්ෂව ඉදිරියෙන්ද, පසුපසින්ද කියා මැනීමට භාවිතා කරයි.

> **SV = EV − PV**

- **SV = 0:** Project එක Schedule එකට අනුව සිදු වේ (**On Schedule**).
- **SV > 0:** Project එක Schedule එකට වඩා ඉදිරියෙන් ඇත (**Ahead of Schedule**).
- **SV < 0:** Project එක Schedule එකට වඩා පසුපසින් ඇත (**Behind Schedule**).

#### 2. Schedule Performance Index (SPI)

Project එකේ Schedule Efficiency එක මැනීමට භාවිතා කරයි.

> **SPI = EV / PV**

- **SPI = 1:** Project එක Schedule එකට අනුව සිදු වේ (**On Schedule**).
- **SPI > 1:** Project එක Schedule එකට වඩා ඉදිරියෙන් ඇත (**Ahead of Schedule**).
- **SPI < 1:** Project එක Schedule එකට වඩා පසුපසින් ඇත (**Behind Schedule**).

#### 3. Cost Variance (CV)

Project එකේ වියදම් Budget එකට සාපේක්ෂව පාලනය වී තිබේද කියා මැනීමට භාවිතා කරයි.

> **CV = EV − AC**

- **CV = 0:** Project එක Budget එකට අනුව සිදු වේ (**On Budget**).
- **CV > 0:** සැලසුම් කළ මුදලට වඩා අඩුවෙන් වැය වී ඇත (**Under Budget**).
- **CV < 0:** සැලසුම් කළ මුදලට වඩා වැඩියෙන් වැය වී ඇත (**Over Budget**).

#### 4. Cost Performance Index (CPI)

Project එකේ Cost Efficiency එක මැනීමට භාවිතා කරයි.

> **CPI = EV / AC**

- **CPI = 1:** Project එක Budget එකට අනුව සිදු වේ (**On Budget**).
- **CPI > 1:** Project එකේ වියදම් කාර්යක්ෂමයි (**Cost Efficient / Under Budget**).
- **CPI < 1:** Project එකේ වියදම Budget එක ඉක්මවා ඇත (**Cost Overrun / Over Budget**).

### Quick Summary

- **SV:** `EV − PV` — Schedule Performance මැනීම.
- **SPI:** `EV / PV` — Schedule Efficiency මැනීම.
- **CV:** `EV − AC` — Cost Performance මැනීම.
- **CPI:** `EV / AC` — Cost Efficiency මැනීම.

## 5. Activity Dependency Types

Activities දෙකක් අතර සම්බන්ධතාවය දැක්වීමට පහත Dependency Types භාවිතා කරයි. මෙහි **A** යනු පෙර Activity එක වන අතර **B** යනු එය මත රඳා පවතින Activity එකයි.

1. **Finish-to-Start (FS):** **A** ඉවර වෙනකම් **B** පටන් ගන්න බැහැ.
2. **Start-to-Start (SS):** **A** පටන් ගන්නකම් **B** පටන් ගන්න බැහැ.
3. **Finish-to-Finish (FF):** **A** ඉවර වෙනකම් **B** ඉවර කරන්න බැහැ.
4. **Start-to-Finish (SF):** **A** පටන් ගන්නකම් **B** ඉවර කරන්න බැහැ.

### Quick Reference

- **FS:** Activity **A** Finish වීමෙන් පසුව Activity **B** Start කළ හැකියි.
- **SS:** Activity **A** Start වීමෙන් පසුව Activity **B** Start කළ හැකියි.
- **FF:** Activity **A** Finish වීමෙන් පසුව Activity **B** Finish කළ හැකියි.
- **SF:** Activity **A** Start වීමෙන් පසුව Activity **B** Finish කළ හැකියි.
