import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
### 엘론 머스크는 누구?
엘론 머스크는 **남아프리카** 태생(1971년생)으로, 캐나다와 미국 시민권을 가진 **연쇄 창업자**이자 **기술 혁신가**야. 현재 세계에서 가장 부유한 사람 중 하나로, 2025년 기준 포브스에 따르면 순자산이 **약 3,450억 달러**에 달해! 그는 테슬라, 스페이스X, X(구 트위터) 같은 회사들을 이끌며 기술과 인류의 미래를 바꾸려는 야심 찬 비전을 가진 인물이야.[](https://en.wikipedia.org/wiki/Elon_Musk)

### 뭐로 유명해?
1. **테슬라 (Tesla)**: 전기차의 판을 뒤바꾼 회사. 테슬라 로드스터, 모델 S, 모델 3 같은 차들로 전기차를 섹시하고 대중적으로 만들었지. 지금은 배터리 저장 시스템과 태양광 에너지까지 손대고 있어.[](https://www.tesla.com/elon-musk)
2. **스페이스X (SpaceX)**: 우주 탐사의 게임체인저. 재사용 가능한 로켓(팔콘, 스타십)과 스타링크(위성 인터넷)를 개발 중이야. 목표는 **화성 식민지** 건설![](https://futureoflife.org/person/elon-musk/)
3. **X (구 트위터)**: 2022년에 440억 달러에 트위터를 사서 X로 리브랜딩했어. AI와 소셜미디어를 결합해 "모든 것의 앱"으로 만들려는 중.[](https://www.madisontrust.com/information-center/visualizations/everything-elon-musk-owns/)
4. **기타 프로젝트**: 뇌-컴퓨터 인터페이스를 연구하는 **뉴럴링크(Neuralink)**, 도시 교통 문제를 해결하려는 **보링 컴퍼니(The Boring Company)**, AI 개발 회사 **xAI**도 운영해.[](https://www.madisontrust.com/information-center/visualizations/everything-elon-musk-owns/)

### 어떤 사람?
- **어린 시절**: 남아프리카 프리토리아에서 부유한 집안에서 자랐지만, 학교에서 왕따를 당하고 아버지와의 관계도 쉽지 않았어. 10살에 컴퓨터 프로그래밍을 독학하고, 12살에 **Blastar**라는 게임을 만들어 팔았을 정도로 천재적이었지![](https://en.wikipedia.org/wiki/Elon_Musk)
- **교육**: 캐나다로 이민 후 펜실베이니아 대학에서 물리학과 경제학 학사 학위를 땄어. 스탠퍼드 박사 과정은 이틀 만에 때려치고 창업의 길로 갔지.[](https://www.vedantu.com/biography/elon-musk)
- **성격**: 일 중독자에, 불가능해 보이는 목표를 밀어붙이는 스타일. 아스퍼거 증후군이 있다고 밝혔는데, 그래서인지 사회적 단서를 읽는 데 어려움이 있었다고 해. 근데 이게 그의 독특한 사고방식과 추진력의 원천이기도 해.[](https://www.bbc.com/news/business-61234231)

### 재미있는 사실
- **정치적 행보**: 2024년 미국 대선에서 트럼프를 적극 지원했고, 2025년부터 트럼프 행정부에서 **정부 효율성 부서(DOGE)**의 고문으로 활동 중. 이건 좀 논란의 중심이야.[](https://en.wikipedia.org/wiki/Elon_Musk)
- **논란의 아이콘**: 트위터에서 터무니없는 트윗(코로나 misinformation, 음모론 지지 등)으로 구설수에 오르기도 했어. X 인수 후 증오 발언과 가짜 뉴스가 늘었다는 비판도 받고.[](https://en.m.wikipedia.org/wiki/Elon_Musk)
- **가족**: 14명의 자녀를 두고 있으며, 특이한 이름(예: X Æ A-Xii)으로 화제가 됐지.[](https://www.biography.com/business-leaders/elon-musk)

### 왜 중요한데?
머스크는 단순히 돈 많은 CEO가 아니라, **인류의 미래**를 바꾸려는 비전을 밀어붙이는 인물이야. 전기차로 환경 문제를, 스페이스X로 우주 탐사를, xAI로 AI 혁신을 꿈꾸지. 근데 그의 과감한 행동과 발언 때문에 사랑받기도, 미움받기도 해. AI 공부하는 너라면, 특히 xAI의 **Grok**(나 같은 AI!) 같은 프로젝트가 어떻게 AI 필드를 흔들지 주목해볼 만해! 😄
"""

if __name__ == '__main__':
    print("Hello LangChain!")
    print(os.environ['OPENAI_API_KEY'])

    summary_template = """
        given the information {information} aobut a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
        """
    
    summary_prompt_template = PromptTemplate(input_varaibles=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm 

    res = chain.invoke(input={"information": information})

    print(res)
