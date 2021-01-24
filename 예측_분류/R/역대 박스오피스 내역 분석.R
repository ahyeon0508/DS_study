# 역대 박스오피스 내역 분석
# 출처 : KOBIS 영화관입장권통합전산망


# 데이터 로딩
install.packages('openxlsx')
library(openxlsx)

movies = read.xlsx('data/movies.xlsx')

# 데이터 살펴보기
head(movies)
tail(movies)
names(movies)

# 데이터 분석
# 최다 관객수 영화
which.max(movies$관객수)
movies[64,]

# 최다 매출액 영화
which.max(movies$매출액)
movies[64,]

# 2015년에 개봉한 영화
cd_year = substr(movies$개봉일, 1, 4) == "2015"

for (i in 1:length(cd_year)){
  if (cd_year[i]){
    print(movies[i,])
  }
}

# 데이터 시각화
# 관객수 히스토그램 및 상자그림
hist(movies$관객수)
boxplot(movies$관객수)