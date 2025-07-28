# Final_Ethic

# 🤖 EthicProject: AI 윤리 융합 수업 웹앱

> **"AI 돌봄 로봇, 효도일까 방임일까?"**  
> 중학생 대상의 AI + 윤리 융합 수업을 위해 제작된 Streamlit 기반 웹앱입니다.

---

## 🗂️ 웹앱 구성

| 페이지 | 설명 |
|--------|------|
| **Main** | 수업 주제 및 전체 웹앱 소개 |
| **AI_Ethics** | AI 윤리 수업 활동 진행: 돌봄 로봇 윤리 문제 탐구 및 의견 작성 |
| **ElderEmotionsAI** | 노인 감정 분석 AI 체험: 표정 분석 결과에 따른 돌봄 행동 추천 |

---

## 🎓 교육적 목적

- AI 기술과 윤리적 사고를 연결하여 **비판적 사고력** 함양
- 노인 돌봄이라는 현실적 주제를 통해 **AI 윤리 문제를 실제처럼 체험**
- **학생 참여형 수업 설계**를 위한 보조 도구 제공

---

## 🌐 웹앱 사용법

```bash
# 필수 라이브러리 설치
pip install streamlit pandas requests pillow

# 실행
streamlit run app.py


---

### 📌 추가 팁

- `assets/` 폴더에 `main_page.png`, `emotion_result.png` 스크린샷 이미지 저장하면 시각적 완성도 높아져!
- 프로젝트를 `streamlit run` 하면 사이드바 메뉴로 여러 페이지 이동 가능해.
- `requirements.txt`도 같이 올리면 좋음:

```txt
streamlit
pandas
requests
Pillow

