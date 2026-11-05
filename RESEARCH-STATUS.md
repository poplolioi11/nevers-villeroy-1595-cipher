# v0.1.2 研究現況補充（2026-11-05）

本函仍未破解，沒有新增確認明文、接受金鑰或提高校讀。本版只新增公開文獻、獨立通用教學例及有限原書地址重播，目標轉用未通過。既有公開資料及下方原已公開的說明／數字保留；後續私有數據、候選與流程未加入。新入口見PERIOD-CONSTRUCTIONS.md及examples/composition/README.md。

---

# 研究現況與方法限制 / Research status and limitations

更新日期：2026-11-04。版本v0.1.1是研究文件更新；沿用v0.1.0的公開符號轉錄與R1／R2結果，沒有重新轉錄、改字或提升校讀等級。**本函仍未解，沒有經獨立驗證的目標金鑰或新增明文。**

## 後續研究做了什麼

| 工作 | 高層結果及限制 |
|---|---|
| 原尺度影像 | 後續已取得館方原尺度圖塊，組成閱覽用拼圖，改善早期小型閱覽圖的限制。拼圖不等於館方整張JPEG原始bytes；本包不附影像。 |
| 符號與附標 | 比較跨行字形、連寫、圈、短豎、點與橫，保留不確定碼界。外形相近、外形清楚或固定輸入均不代表已知字值；後續逐符工作資料未加入本版。 |
| 代換與結構 | 檢查代換、重複結構及外部碼表的有限假說。有些方法在相近已知材料上先暴露能力不足，不能用它們在目標失敗排除整個密碼家族。 |
| 音節／詞碼混合 | 以已知金鑰與真實密函測局部查表及混合碼讀法。局部控制成立不代表能恢復未知金鑰，也不證本函與參照材料同鑰。 |
| 語言與碼界 | 語言分數高仍可能把正確碼拆錯；允許更多數碼對應會增加覆蓋，但不構成正確率。未把未通過控制的方法輸出採為本函明文。 |
| 跨行一致性 | 重複碼可用來檢查矛盾；缺獨立明文錨點時，同一組字值候選也可能讓所有切分保持一致，增加枚舉並不自動提供辨識力。 |
| 數字串與標記 | 數字視窗含某二位數，不足以證實該二位數是一碼。比較碼表時，字身、離體橫／點、姓名詞碼及其他記法需分開，不因語意合適補標記。 |
| 其他金鑰與已知函 | 取得1591年no36碼表的可讀出版物複製圖，並確認一封1591年已知函的館藏與刊本定位；原件密碼及手寫解文尚未取得，來源表讀值未因此升為本函對應。 |

## 可以沿用與仍待證明的部分

公開的初錄、疑讀、必要定位及R1／R2結果可供逐位核對、提出不同假說與訂正。後續原尺度影像取得及來源追索的狀態，提供接續研究方向，但不表示這些影像或後續私有轉錄已包含在下載包。

主要缺口已由早期取圖轉向可靠分碼、附標身分，以及本函與某把金鑰的實際關係。需要能區分競爭假說的新證據，例如同函明文、手寫解文或經獨立材料檢驗的局部對應。S樣形作數字5等讀法仍未確定；沒有因套表出現零星法文而接受讀法。

來源未取得、有限搜索查無用例、求解器失敗，都不能推成原件不存在、全球未解、某類系統已排除或本函不可解。AI讀圖、模型一致、程式及格式檢查也不等於人類二校或專家審定。

本文件只公開理解成果所需的高層方法與失敗意義。原圖、裁片、後續逐符工作資料、完整候選、專用程式、參數、提示、私人通信及完整工作紀錄不在公開包；不能由此包完整重跑製作流程。分層權利見[RIGHTS.md](RIGHTS.md)。

## English summary

Version 0.1.1 updates research documentation while retaining the public transcription and R1/R2 result files from version 0.1.0 byte for byte. It adds no plaintext, accepted target key, new transcription or higher collation status.

Subsequent research obtained original-scale library image tiles and assembled viewing mosaics. These mosaics are not the library's original whole-image JPEG files, and no images are distributed here. Cross-line comparison retained uncertainties in ligatures, circles, stems, dots, strokes and code boundaries; later working transcriptions are not included in this release.

Substitution, structural, mixed syllable/word-code, language and segmentation hypotheses were examined using known materials where available. Some methods failed capability checks before target application. Successful local lookups with a known key do not demonstrate unknown-key recovery or establish that this letter uses that key. High language scores and increased dictionary coverage may result from incorrect segmentation. Repeated-code consistency without independent anchors can leave competing segmentations unresolved. An overlapping two-digit window is not itself an attested code use, and semantic appeal does not justify restoring marks.

A readable publication reproduction of the 1591 no36 table and catalogue/printed-edition locations for a known letter were obtained. The actual letter's cipher and handwritten decipherment remain unavailable to this study, so table readings have not become validated target correspondences. Reliable boundaries, marks and independent evidence connecting a key to this letter remain the main needs. Failed retrievals or solvers do not establish absence or impossibility. The dataset remains provisional and has not undergone full human collation; private images, software, prompts and full working records are excluded.

## 參照來源 / References

- 目標原件：[BnF Français3993 no.102，view161](https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f161.item)、[view162](https://gallica.bnf.fr/ark:/12148/btv1b9059229n/f162.item)。Source gallica.bnf.fr / Bibliothèque nationale de France。
- 歷史碼表參照：[Tomokiyo的Nevers碼表目錄](https://cryptiana.web.fc2.com/code/nevers.htm)；不同編號不是同一把鍵的證明。
- Desenclos與Lasry，2024，*An early French digit cipher: deciphering a letter from the King of France to the Duke of Nevers (1592)*，[機構條目](https://dspace.ut.ee/items/cb0c82a2-1db7-4ce1-9ae7-8d40c3043e5b)。該篇附錄收有no36表，不能把1592函當1591函。
- 1591已知函定位：[BnF原印目錄，印頁591–594](https://archive.org/details/p1cataloguegnr02bibluoft)；[《Recueil》卷III，印頁377–379](https://archive.org/details/recueildeslettre03henr)。刊本中的編者猜補不當作原件已讀明文。
