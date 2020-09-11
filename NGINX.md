
硬體式 F5
NGINX 與 Application 在一起，並非取代硬體的角色
軟體的還是需要，類似 ingress 的角色

第一層
開源軟體負載平衡器，依 http 碼 206 快取
依路徑分流快取 direct

## 微服務
* 作為 ingress controller 的角色，直接用 nginx 來取代掉。
* 版本差異
  * 原廠保固、弱點或 BUG 修復、Controller manages(config, GUI) - 傳統 command line 取代來管 NGINX plus
  * NGINX plus 節點、效能
  * NGINX response time 的資訊

NGINX Plus API Gateway
* Controller control
* 一秒鐘只能存取幾次
* 驗證與授權部份 - 對外, JWTs
* API Dashbaord
* 


Clair 
* 掃 container 的 base image / application - runtime
* NFS PV 在上面 
* Deploy - container 佈署一個 pod 上去會作 yaml 檔，會把 yaml 檔參數化，動態餵進去參數然後 deploy
* VMbase vs Container
* 每個 branch 都要 build
* IQ Server 是存在肚子無法抓，但 Clair 有 API 可以抓，設定 threshold 條件


K8s
* Deployment
* Service
* ConfigMap
* 

Helm2 --> 3
管理 K8s 的管理工具 - Chart, Config, Release

Ansible - 自動化管理工具 + k8s module
Shell script - 主要原因為作遠端控制、買了 Ansible tower(權限及執行結果控管)

kubecontrol - 同一個腳本一個 playbook 作完一件事，存在 gitlab for code version





