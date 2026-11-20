import pandas as pd
def 정제(df):
    정제_df = df.copy()
    print(f"시작: {len(정제_df)}행")

    # 점수가 비어 있는 행을 삭제한다.
    정제_df = 정제_df.dropna(subset=["점수"])
    print(f"점수 결측 행 삭제 후: {len(정제_df)}행")

    # 모든 열의 값이 같은 중복 행을 하나만 남긴다.
    정제_df = 정제_df.drop_duplicates()
    print(f"중복 행 삭제 후: {len(정제_df)}행")

    # 반과 과목 값의 앞뒤 공백을 제거한다.
    for 열 in ["반", "과목"]:
        정제_df[열] = 정제_df[열].str.strip()
    print(f"공백 제거 후: {len(정제_df)}행")

    # 점수가 0~100 범위 밖인 행을 삭제한다.
    정제_df = 정제_df[정제_df["점수"].between(0, 100)]
    print(f"점수 범위 확인 후: {len(정제_df)}행")

    return 정제_df

df = 정제(pd.read_csv("scores_2026.csv"))

# 수학 과목만 남기기
df_math = df[df["과목"] == "수학"]
print(len(df_math))

# 1반이면서 90점 이상인 행만 남기기
df_1반_90점이상 = df[(df["반"] == "1반") & (df["점수"] >= 90)]
print(len(df_1반_90점이상))

# 반별 점수 평균
반별_평균 = df.groupby("반")["점수"].mean()
print(반별_평균)

# 과목과 반별 점수 평균
과목_반별_평균 = df.groupby(["과목", "반"])["점수"].mean()
print(과목_반별_평균)

def 반별평균(df):
    표 = df.groupby("반").agg(
        개수=("점수", "count"),
        평균=("점수", "mean"),
        중앙값=("점수", "median"),
        최댓값=("점수", "max"),
    ).round(2)

    print(표)
    return 표["평균"].to_dict()


반별평균(df)

미니 = 정제(pd.read_csv("mini.csv"))
print(반별평균(미니))