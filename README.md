# ArabicTranscriber
A rule-based Arabic transcriber which can be adapted to dialects.

Arabic Transcriber attempts to bring Arabic text, which could be assumed to be in the standard language (FuS7a) or a dialect, into a canonical representation, and then transcribe it into the target alphabet. The canonical representation is based on the Arabic alphabet and auxiliary vowelization marks (Tashkil), adding letters which are conventionally used to represent sounds not existent in the standard language variety but used in dialects, such as G used in Egyptian or CH used in some dialects.
Custom rules can be applied in the process of converting from the common written representation to the canonical representation:
   * substituting some letters with those representing their actual pronunciation in a particular dialect, e.g. Qaf becoming Hamza in many dialects or Jim and Ghayn becoming G in Egyptian.
   * Substituting Tanween with a phonetic representation
   * L becoming a Shadda when the article AL is applied to "sun-letters".
Initially the target language is Hebrew, since the principles of its orthography are very similar to Arabic, hence ambiguities in the source text could be left as such in the resulting transcription.

Rules can also be applied in the target script. e.g. in Hebrew change certain letters to their final form where needed.
