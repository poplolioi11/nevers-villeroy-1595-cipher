# Nevers 致 Villeroy 密函（1595）：部分符號轉錄與有限枚舉紀錄

## 摘要 / Abstract

1595年8月16日Nevers致Villeroy函保存於法國國家圖書館Français 3993第102件、148r–149r葉。本資料提供部分視覺符號初錄、疑讀、來源定位與早期有界枚舉結果，以JSON、TXT及最小TEI投影保存。v0.1.2新增十六世紀密碼構成法的來源提要、Porta 1563原書範例的地址層校驗，以及從零撰寫的通用合成示例與反例。既有16個資料、轉錄及早期結果檔沿用原位元內容。本函仍無經獨立驗證的金鑰或新增明文，未完成人類全文校讀。

The Nevers–Villeroy letter of 16 August 1595 is held by the Bibliothèque nationale de France, Français 3993, no. 102, folios 148r–149r. This dataset provides partial visual-symbol observations, uncertainty, source locations and early bounded enumeration results in JSON, TXT and a minimal TEI projection. Version 0.1.2 adds a source guide to sixteenth-century cipher constructions, address-level checks of Porta’s 1563 printed example, and newly written generic synthetic demonstrations and a counterexample. The 16 existing data, transcription and early-result files retain their original bytes. No independently validated target key or new plaintext is supplied, and full human collation remains incomplete.

**尚未解密 / Not deciphered.** v0.1.2為研究文件更新；原公開轉錄未改，不表示二校或定稿。

整理者：曲宸宇（Chu, Chen-Yu；GitHub：poplolioi11），[ORCID](https://orcid.org/0009-0003-9738-6914)。歷史寄信人、收信人、原館藏與現代整理者的角色各自分開。

## v0.1.2 新增內容 / New material

[年代方法來源](PERIOD-CONSTRUCTIONS.md)區分Porta的整格雙字替換、四位置合字及格形點數碼，另列Alberti、Trithemius、Bellaso與待核來源。文獻描述不等於本函使用證據；autokey及Cardano格柵原段仍待核。

[通用示例](examples/composition/README.md)提供合成正反例與Porta1563原書前綴的地址重播。相同部件幾何可相容於不同字值結構；沒有完成原glyph全串驗證，也沒有通過本函轉用。這些全新通用程式依目錄內MIT授權，原創資料說明與編排沿用CC BY4.0；不包含私有處理流程。

The new bibliography separates historical constructions and unresolved source checks. Independent synthetic controls and limited period-example address replay are reproducible, but do not establish historical glyph reproduction or target decipherment. The new generic programs have a separate MIT license; documentation and arrangement retain their scoped CC BY4.0 terms.

## 範圍與目前狀態

取文來源為 [Gallica 第 161 視圖](https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f161.item)右半的 f.148r，以及[第 162 視圖](https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f162.item)的 f.148v–149r（148v 為依頁序推定）。v0.1.0製作時使用涵蓋三面的兩張閱覽圖，尺寸為1285×1054與1289×1054。後續研究已取得館方原尺度圖塊並組成閱覽拼圖；拼圖不等於館方整張JPEG原始bytes。本版公開轉錄仍保留原快照，未自動提升為原尺度二校結果。本公開包不附來源影像、裁片或完整第三方 OCR 語料。

- 舊批次保留 309 個暫存位置，逐位外形覆核後為 305 外形清楚、4 外形疑讀；另有 73 位置涉及分組或用途疑義。數字或字母身分、明文值仍未確定。
- 新兩面保留隔離初讀 A、B，各 506、503 個視覺暫存單位；切分方式不同，差額不是漏字數，也不是準確率。19 個物理行對齊後作 30 項有限裁定，7 接受、23 未解；其他未逐位裁定位置仍未裁定，沒有整份合併定稿。
- 全頁盤點按自然文中斷分成 14 個連續密碼片段。這與前人 17 runs 的定義不同，不能直接比較成漏錄數。孤立數字及是否屬密碼的行尾筆畫仍保留未定。
- R1 的嚴格疑義篩選分支沒有合格視窗，零候選不構成反證；暫存敏感度分支有 2515 筆局部樣式相容記錄，均未接受。
- R2 測試外部 key76 部分對齊的 576 組有限參數，其中 384 組有可評分窗口。這些不是 576 把獨立完整金鑰。尚無獨立證據接受本封金鑰。

以上數字各有不同範圍和單位，不相加成全文字數或已解字數。自然文、日期、簽名、全部副文本與整封法文正文尚未完整轉錄。

後續研究現況、已知材料控制及失敗限制，見[RESEARCH-STATUS.md](RESEARCH-STATUS.md)。本版新增高層說明、公開來源與通用示例，不加入後續私有逐符資料或完整試驗輸出。

## 檔案入口

| 路徑 | 內容 |
|---|---|
| `data/` | 逐符觀察、A/B 分稿、有限裁定、版面盤點及來源資料 |
| `transcriptions/` | 從 JSON 確定性匯出的 TXT；若附 TEI，僅為最小視覺符號投影 |
| `results/` | R1 嚴格／暫存分支與 R2 有限枚舉輸出，所有候選標示未接受 |
| [RESEARCH-STATUS.md](RESEARCH-STATUS.md) | 後續研究摘要、可沿用成果與未解依賴 |
| [METHODS.md](METHODS.md) | 為何測這些假設、已測範圍、結果與未測範圍 |
| [READING-GUIDE.md](READING-GUIDE.md) | 符號、未知、座標、檔案對照與使用限制 |
| [PROVENANCE.md](PROVENANCE.md) | 原館藏、前人研究、外部 key76 及語料來源 |
| [RIGHTS.md](RIGHTS.md) | 分層權利與本次非營利公開範圍 |
| [FAILURES.md](FAILURES.md) | 取得影像及研究中的失敗與結果限制 |

JSON 是資料主本，TXT 的空白、換行與分隔不是原件標點。請一併保存 sidecar、版本及疑讀資訊。完整結果不是可讀明文，不能將最高分候選當作翻譯。

## 品質、方法與訂正

既有影像初讀、隔離替代讀法及有限裁定由AI助手輔助完成，主代理整理與編碼。本次只整理文件，沒有重新判字；工具未完整回報實際模型識別，不把請求型號當作執行證據。本機 Python 實際執行枚舉與數值核對。兩稿比較後的裁定不再稱盲讀；模型一致、雜湊、格式檢查與合成控制都不代替人類校讀。

依公開範圍只提供理解成果所需的高層方法與枚舉結果。專用處理程式、詳細流程、提示詞、內部模板、完整派工／驗收歷程及私人資料保持私有；本包不承諾能重跑全部製作流程。這些限制不妨礙對公開資料逐位訂正或提出不同密碼假設。

請在 [Issues](https://github.com/poplolioi11/nevers-villeroy-1595-cipher/issues) 提供版本、資料 ID、官方原頁、近似 bbox、原讀法與建議，以及圖像理由。候選讀法與接受的訂正分開；後續實質改字以新版本留差異，保留本固定版。

## 權利與引用

Source gallica.bnf.fr / Bibliothèque nationale de France。

本次為非營利研究公開。自有具著作權的說明與編排採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；歷史原文及不受著作權保護的事實不主張新增權利。此授權不覆蓋第三方來源，亦不代 BnF 授權來源影像、完整 OCR、商業或 AI 再利用；請閱讀 [RIGHTS.md](RIGHTS.md)。

本版v0.1.2更新研究文件；轉錄及R1／R2資料仍是首次公開版v0.1.0的快照，**版號不表示二校完成**。引用現代資料時使用整理者 Chu, Chen-Yu、資料標題、版本及固定 release URL；勿將其列作歷史原作者。機讀引用見 [CITATION.cff](CITATION.cff)。

關鍵字：歷史密碼、符號轉錄、未解密函、同音替換、諾芒克拉托／詞碼、法國書信史、Nevers、Villeroy、1595、historical cryptography、cipher transcription、homophonic cipher、nomenclator、digital humanities、uncertainty annotation。

固定舊版DOI：[v0.1.0](https://doi.org/10.5281/zenodo.23861009)。本版固定引用以[CITATION.cff](CITATION.cff)及[發行頁](https://github.com/poplolioi11/nevers-villeroy-1595-cipher/releases/tag/v0.1.2)為準。

本版版本DOI：[10.5281/zenodo.23969835](https://doi.org/10.5281/zenodo.23969835)。製備時已預留，正式發布狀態以[Zenodo紀錄](https://zenodo.org/records/23969835)為準。
