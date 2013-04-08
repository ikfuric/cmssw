import FWCore.ParameterSet.Config as cms

ecalDQMCollectionTags = cms.untracked.PSet(
    Source = cms.untracked.InputTag("rawDataCollector"),
    EcalRawData = cms.untracked.InputTag("ecalEBunpacker"),
    GainErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityGainErrors"),
    ChIdErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityChIdErrors"),
    GainSwitchErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityGainSwitchErrors"),
    TowerIdErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityTTIdErrors"),
    BlockSizeErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityBlockSizeErrors"),
    MEMTowerIdErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityMemTtIdErrors"),
    MEMBlockSizeErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityMemBlockSizeErrors"),
    MEMChIdErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityMemChIdErrors"),
    MEMGainErrors = cms.untracked.InputTag("ecalEBunpacker", "EcalIntegrityMemGainErrors"),
    EBSrFlag = cms.untracked.InputTag("ecalEBunpacker"),
    EESrFlag = cms.untracked.InputTag("ecalEBunpacker"),
    EBDigi = cms.untracked.InputTag("ecalEBunpacker", "ebDigis"),
    EEDigi = cms.untracked.InputTag("ecalEBunpacker", "eeDigis"),
    PnDiodeDigi = cms.untracked.InputTag("ecalEBunpacker"),
    TrigPrimDigi = cms.untracked.InputTag("ecalEBunpacker", "EcalTriggerPrimitives"),
    TrigPrimEmulDigi = cms.untracked.InputTag("simEcalTriggerPrimitiveDigis"),
    EBUncalibRecHit = cms.untracked.InputTag("ecalGlobalUncalibRecHit", "EcalUncalibRecHitsEB"),
    EEUncalibRecHit = cms.untracked.InputTag("ecalGlobalUncalibRecHit", "EcalUncalibRecHitsEE"),
    EBRecHit = cms.untracked.InputTag("ecalRecHit", "EcalRecHitsEB"),
    EERecHit = cms.untracked.InputTag("ecalRecHit", "EcalRecHitsEE"),
    EBBasicCluster = cms.untracked.InputTag("hybridSuperClusters", "hybridBarrelBasicClusters"),
    EEBasicCluster = cms.untracked.InputTag("multi5x5SuperClusters", "multi5x5EndcapBasicClusters"),
    EBSuperCluster = cms.untracked.InputTag("correctedHybridSuperClusters"),
    EESuperCluster = cms.untracked.InputTag("multi5x5SuperClusters", "multi5x5EndcapSuperClusters")
)
