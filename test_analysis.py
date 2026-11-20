import pandas as pd

from analysis import 정제, 반별평균

scores_df = pd.read_csv("scores_2026.csv")
mini_df = pd.read_csv("mini.csv")

정제_scores = 정제(scores_df)
정제_mini = 정제(mini_df)


def test_scores_정제후_100행():
    assert len(정제_scores) == 100


def test_반은_1반과_2반뿐이다():
    assert set(정제_scores["반"].unique()) == {"1반", "2반"}


def test_반별_점수합과_전체_점수합이_같다():
    반별_합계 = 정제_scores.groupby("반")["점수"].sum().sum()
    assert 반별_합계 == 정제_scores["점수"].sum()


def test_mini_1반_평균은_80이다():
    assert 반별평균(정제_mini)["1반"] == 80.0