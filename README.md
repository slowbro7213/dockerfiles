Dockerfile 저장소
=============

hadoop
-------------
###### hadoop 클러스터 노드
* 3.3.4-focal

javabuild
-------------
###### gradle 을 사용한 java 빌드

python-cron
-------------
###### python 애플리케이션의 배치 사용
* apscheduler: pythonn 패키지 사용
  * 컨테이너 실행 시 -e TZ 로 timezone 맞출 것.
  * 함수 사용 안정적.
  * BlockingScheduler 를 사용하면 데몬처럼 동작하므로 daemon 패키지는 불필요.
* service: 컨테이너 내부 cron 사용.
  * 컨테이너 실행 시 -e TZ 로 timezone 맞출 것.
  * cron 으로 실행한 스크립트의 함수 호출이 불안정함.
