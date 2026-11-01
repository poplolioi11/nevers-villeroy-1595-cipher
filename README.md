# Nevers 致 Villeroy 密函（1595）：部分符號轉錄與有限枚舉紀錄

**尚未解密。** 本資料公開 BnF Français 3993 no. 102、1595 年 8 月 16 日密函的部分符號初錄、疑讀、來源定位及有限金鑰假設的實驗結果，供後續研究、核對與訂正。沒有已驗證的新金鑰或新增明文，也未經人類全文二校、專家審定或同儕審查。

This dataset contains provisional visual-symbol transcriptions and bounded experimental outputs for the Nevers–Villeroy letter dated 16 August 1595. **It is not a decipherment.** Candidate outputs are unaccepted; the material is not human-collated.

整理者：曲宸宇（Chu, Chen-Yu；GitHub：poplolioi11），[ORCID](https://orcid.org/0009-0003-9738-6914)。歷史寄信人、收信人、原館藏與現代整理者的角色各自分開。

## 範圍與目前狀態

取文來源為 [Gallica 第 161 視圖](https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f161.item)右半的 f.148r，以及[第 162 視圖](https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f162.item)的 f.148v–149r（148v 為依頁序推定）。研究取得涵蓋三面的兩張完整頁面範圍閱覽圖，尺寸為 1285×1054 與 1289×1054；**未取得原生高解析度 JPEG**。本公開包不附來源影像、裁片或完整第三方 OCR 語料。

- 舊批次保留 309 個暫存位置，逐位外形覆核後為 305 外形清楚、4 外形疑讀；另有 73 位置涉及分組或用途疑義。數字或字母身分、明文值仍未確定。
- 新兩面保留隔離初讀 A、B，各 506、503 個視覺暫存單位；切分方式不同，差額不是漏字數，也不是準確率。19 個物理行對齊後作 30 項有限裁定，7 接受、23 未解；其他未逐位裁定位置仍未裁定，沒有整份合併定稿。
- 全頁盤點按自然文中斷分成 14 個連續密碼片段。這與前人 17 runs 的定義不同，不能直接比較成漏錄數。孤立數字及是否屬密碼的行尾筆畫仍保留未定。
- R1 的嚴格疑義篩選分支沒有合格視窗，零候選不構成反證；暫存敏感度分支有 2515 筆局部樣式相容記錄，均未接受。
- R2 測試外部 key76 部分對齊的 576 組有限參數，其中 384 組有可評分窗口。這些不是 576 把獨立完整金鑰。尚無獨立證據接受本封金鑰。

以上數字各有不同範圍和單位，不相加成全文字數或已解字數。自然文、日期、簽名、全部副文本與整封法文正文尚未完整轉錄。

## 檔案入口

| 路徑 | 內容 |
|---|---|
| `data/` | 逐符觀察、A/B 分稿、有限裁定、版面盤點及來源資料 |
| `transcriptions/` | 從 JSON 確定性匯出的 TXT；若附 TEI，僅為最小視覺符號投影 |
| `results/` | R1 嚴格／暫存分支與 R2 有限枚舉輸出，所有候選標示未接受 |
| [METHODS.md](METHODS.md) | 為何測這些假設、已測範圍、結果與未測範圍 |
| [READING-GUIDE.md](READING-GUIDE.md) | 符號、未知、座標、檔案對照與使用限制 |
| [PROVENANCE.md](PROVENANCE.md) | 原館藏、前人研究、外部 key76 及語料來源 |
| [RIGHTS.md](RIGHTS.md) | 分層權利與本次非營利公開範圍 |
| [FAILURES.md](FAILURES.md) | 取得影像及研究中的失敗與結果限制 |

JSON 是資料主本，TXT 的空白、換行與分隔不是原件標點。請一併保存 sidecar、版本及疑讀資訊。完整結果不是可讀明文，不能將最高分候選當作翻譯。

## 品質、方法與訂正

影像初讀、隔離替代讀法及有限裁定由 OpenAI 原生模型助手完成；複雜讀形使用 gpt-6-astra，主代理整理與編碼。本機 Python 實際執行枚舉與數值核對。兩稿比較後的裁定不再稱盲讀；模型一致、雜湊、格式檢查與合成控制都不代替人類校讀。

依公開範圍只提供理解成果所需的高層方法與枚舉結果。專用處理程式、詳細流程、提示詞、內部模板、完整派工／驗收歷程及私人資料保持私有；本包不承諾能重跑全部製作流程。這些限制不妨礙對公開資料逐位訂正或提出不同密碼假設。

請在 [Issues](https://github.com/poplolioi11/nevers-villeroy-1595-cipher/issues) 提供版本、資料 ID、官方原頁、近似 bbox、原讀法與建議，以及圖像理由。候選讀法與接受的訂正分開；後續實質改字以新版本留差異，保留本固定版。

## 權利與引用

Source gallica.bnf.fr / Bibliothèque nationale de France。

本次為非營利研究公開。自有具著作權的說明與編排採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；歷史原文及不受著作權保護的事實不主張新增權利。此授權不覆蓋第三方來源，亦不代 BnF 授權來源影像、完整 OCR、商業或 AI 再利用；請閱讀 [RIGHTS.md](RIGHTS.md)。

本版為第一個公開版 v0.1.0，對應私人研究至第 0.2 輪，**版號不表示二校完成**。引用現代資料時使用整理者 Chu, Chen-Yu、資料標題、版本及固定 release URL；勿將其列作歷史原作者。機讀引用見 [CITATION.cff](CITATION.cff)。

關鍵字：歷史密碼、符號轉錄、未解密函、同音替換、諾芒克拉托／詞碼、法國書信史、Nevers、Villeroy、1595、historical cryptography、cipher transcription、homophonic cipher、nomenclator、digital humanities、uncertainty annotation。

固定資料 DOI：`10.5281/zenodo.23861009`。本包製備時預留，是否正式發布請核對[Zenodo紀錄](https://zenodo.org/records/23861009)。
