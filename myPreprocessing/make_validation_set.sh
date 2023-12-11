# mv ${spec_root}/p226_*.wav ${spec_root}/valid
# mv ${spec_root}/p287_*.wav ${spec_root}/valid

src_dir = "/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/train"
dst_dir = "/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/valid"


mv ${src_dir}/clean/p226_*.wav ${dst_dir}/clean
mv ${src_dir}/clean/p287_*.wav ${dst_dir}/clean

mv ${src_dir}/noisy/p226_*.wav ${dst_dir}/noisy
mv ${src_dir}/noisy/p287_*.wav ${dst_dir}/noisy

# mv /misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/train/noisy/p287_*.wav /misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/valid/noisy

# 有报错，未解决
# bash: ./make_validation_set.sh: Permission denied