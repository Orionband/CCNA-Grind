import json

def set_difficulty(questions):
    """
    Manually assesses each question and assigns a new difficulty level.
    """
    difficulty_updates = {
        "F88A5841-6905-4658-90AC-00E7EFE9DBCE": 1, # Basic recall of beacon frame purpose.
        "91CDCDD9-F50C-452F-9168-0169C0034AC7": 1, # Recall of Wi-Fi Alliance's role in compatibility names.
        "292F8622-4890-43C1-8E8F-20E10B463D97": 1, # Basic recall of IEEE 802.11 standard.
        "D8BF83DE-0B30-4270-BB29-2158BF15C224": 1, # Basic definition of ESSID.
        "617DABF2-D0CA-470F-AA6E-2AFBAE94A6A6": 1, # Recall of common Wi-Fi frequency bands.
        "558C5D85-81D8-4FBF-A3B9-2E0A78D1B8CC": 1, # Understanding wireless communication on a single frequency (one transmit, many receive).
        "62FB1CEE-3C9F-492C-A2D4-388436A3A3E7": 1, # Recall of SSID consistency for roaming.
        "54A700F9-5C90-48B7-A2F4-3AF90C8B3ACE": 1, # Understanding SSID vs. BSSID uniqueness.
        "E29C5581-56EC-4E22-A7EE-48FE7274903D": 2, # Identifying non-overlapping Wi-Fi channels.
        "68522238-F1A0-42BA-89A8-4CBDB22ED2A4": 1, # Basic definition of SSID.
        "868FFBD9-C501-4E5A-A01B-50478644875E": 1, # Recall of beacon frame transmission frequency.
        "C2E3A484-3306-4FE8-883C-54A4140A2FC5": 1, # Device providing a basic service set.
        "525F38C5-2B6C-416A-85E0-5B710EA665F5": 1, # BSSID looks identical to which other network parameter.
        "F8E18427-3DCF-474F-BA7A-883024C4D629": 2, # Identifying valid non-overlapping channel lists.
        "9ED13918-FF52-4B5A-B17E-AAC96F9E7C08": 1, # Correct strategy for non-overlapping Wi-Fi channels.
        "3E6A765F-879B-47FA-BBFF-BA9EAD039DD5": 2, # Understanding Wi-Fi frequency band properties.
        "793C3320-2021-48F2-A49E-BF5C16D83E1A": 1, # Layer 2 destination address for wireless frame to AP.
        "84F3231D-B5F9-4369-8D68-ECB99EE66A7C": 1, # Main frequency bands for wireless LAN.
        "9848F417-1B7E-4C37-B7B9-FA70D82E4E10": 1, # Frequency band for farther propagation.
        "C65B98D9-2689-44D6-976E-FBEF94F490A0": 1, # Wireless device passive scanning purpose.
        "B5654F5F-AFE0-4A70-B2AB-07E6C09808CC": 1, # WLC capabilities.
        "DD52B9CD-221C-4ED1-B739-1A4FBB0170AA": 1, # CAPWAP tunnel termination points.
        "5D76D71A-3166-42C8-AD4E-1AE34D595850": 1, # Definition of EWC.
        "A25C7185-C917-45B8-BB86-1D5640DD61F9": 1, # WLC deployment model supporting least APs.
        "EC438AED-F366-4E33-B3E0-222FD955A033": 1, # Entity handling real-time functions in split-MAC.
        "A5D99619-2EFD-46D7-BC92-2B9B675D3F32": 1, # AP mode for cloud-based WLC deployment.
        "282A3978-3EED-45E7-BA7E-2EDAA199B71F": 1, # Controller deployment supporting least APs.
        "F2B53FE1-E0B4-40B2-B07A-34BED7640EE3": 1, # Normal operating mode of Cisco lightweight AP.
        "05C167DA-73BF-420D-9B11-3678AEED7B81": 1, # Unified WLC deployment model characteristics.
        "FF9CA416-A1D7-49E0-8D4C-3E96C7BE39A4": 1, # Entities in split-MAC wireless architecture.
        "AA31075F-363D-4C67-B178-58848F1BCA05": 2, # Understanding control and data planes in cloud-based AP architecture.
        "7CE22CD7-78A9-4D07-B8FA-61CF8C2FC9AF": 1, # AP modes for operation without WLC.
        "F7E5B80F-CE81-4026-9691-7470550FBB40": 1, # Definition of CAPWAP.
        "84E52D81-4BF4-47F6-BCE6-7B39FBECF53B": 1, # WLC deployment models for best scalability.
        "F0351619-3E01-4F21-B459-8CE2D8E595DE": 1, # AP mode for remote site local network connectivity.
        "6C7E5BF5-8A1E-415C-BBE9-90B017429D5C": 1, # Main difference between FlexConnect and OfficeExtend.
        "D657AC04-2380-4729-A11C-91214057B5F3": 1, # Maximum APs supported by OfficeExtend AP.
        "9DBAB077-0541-4DDD-A536-B3EFFC2678E1": 1, # FlexConnect AP in connected mode characteristics.
        "A63A707A-2D48-47DD-A798-BD4C19844289": 1, # Wireless architecture implied by WLC position.
        "80054481-7A83-47C7-9ED9-C09DAD26984F": 1, # Necessary for autonomous AP to support multiple SSIDs/VLANs.
        "5ADAE3D4-4822-4A1F-BCBC-C29D8F5860F4": 1, # Wireless deployment never requiring WLC.
        "075B02FA-9DC2-4DCD-990D-D77B2235ADC9": 1, # Distributed WLC deployment characteristics.
        "6082EC7E-60AA-4617-B2ED-0253584C4132": 1, # WLC interface for VLAN to WLAN connection.
        "DF4CEA06-FDF8-42AD-A9FD-12E0C338E8DC": 1, # Parameter to configure in policy profile for WLAN.
        "2CF08EEE-7EC4-4D74-974E-139ED95C2CE7": 2, # Wired network link configuration for autonomous vs. lightweight APs.
        "FBC406C6-AD33-4BE8-98EA-143247B6E502": 1, # Traffic type not terminating on IOS-XE controller's wireless management interface.
        "116106CD-9A77-42E4-9A83-36286570882C": 1, # Tags needed to configure WLAN.
        "288DE8E5-E89F-44D1-85A9-3D6DDAD39842": 1, # WLC port for traffic to/from APs.
        "281DEF8E-5E64-4579-8483-40D27D390F89": 1, # Methods to connect to autonomous AP for management.
        "AA6E2F28-76A8-471E-BF3B-52D14011D9C1": 2, # Troubleshooting AireOS WLC LAG with LACP.
        "694FEDEA-5A01-4FC5-8524-612F9F155513": 1, # True statement about IOS-XE controller dynamic interfaces.
        "D53EF76C-B8C3-4356-B2A4-6198A6DEC5C2": 1, # WLC port for forwarding user traffic.
        "6A587A58-AB21-4EB6-94D1-6877BF643A35": 1, # Protocols normally passing through WLC management interface.
        "60B953FC-2099-4679-9888-6BD1B7EDA013": 2, # Configuration areas for dynamic interface and WLAN on AireOS WLC.
        "A57AEA66-FD3A-4FE8-9127-6F69AC66CF12": 1, # Default client limit per AP radio.
        "36367F28-339D-4AC1-ADC1-81A15E53B373": 1, # Maximum characters for SSID string.
        "9D368E3D-C8F2-4ADC-A461-838C61344D43": 1, # Best strategy for WLC distribution system ports.
        "E912D657-2BDF-4826-9250-9316605D3E85": 1, # Traffic type not allowed from WLAN to WLC.
        "7D05DFB2-166F-4792-A1C0-9635D65B1662": 2, # Troubleshooting new WLAN not working (forgotten step).
        "EBC0FE16-9098-4179-9624-9ADBAB3FEDB4": 2, # Configuring WPA2-Personal on WLC GUI.
        "24BE4E70-50A2-4B37-B91B-9FF237D700EA": 1, # AireOS WLC ports vs. interfaces.
        "4A8D1816-B403-49CD-8BE1-AA87D2D6F029": 1, # Correct statements about WLC distribution system port configuration.
        "16722CA8-7EAE-43D1-85D9-B4F9CE18B171": 1, # Default session timeout for wireless clients.
        "C59D17A3-F2CC-4FBE-9C30-B9B75B52A29D": 1, # Number of IP addresses needed on IOS-XE WLC.
        "DBBD2171-2A0D-4288-98A6-DE6EAB369BC7": 1, # What must be identified when configuring new secure WLAN.
        "ECE49A5B-6AFA-4CAF-ADAE-DF60933BA8E3": 1, # Max WLANs configured vs. active on AP.
        "933A52DF-91B8-458B-8A63-EFE64BB6B545": 1, # Wired link type for split-MAC AP.
        "E9854DD2-6B29-475E-8A17-FB3D98E471B9": 2, # WLAN settings with same data format/max length on AireOS WLC.
        "A8BB6E71-E3E6-4601-BE04-C00735A8A99B": 2, # Working methods for IP phone to learn voice VLAN ID.
        "89E04CA3-9350-408C-B5F0-C5702AB90A84": 2, # LLDP-MED vs. LLDP claims.
        "506E40FC-B4D5-4EF2-A4A5-E3864F7636DE": 2, # Outcome of misconfigured CDP timers.
        "4B27AE76-5450-4463-9BE0-1491A395FAEA": 2, # First frame sent by host after boot (ARP broadcast).
        "39EAF550-D2E1-4D70-B772-49EA7A1B1D04": 1, # Default aging time for MAC table entries.
        "46AD8927-BB62-47FA-8D5A-5D071027625E": 1, # What switch compares in MAC table for forwarding.
        "6F912032-AA58-4387-8E68-5E0CE30C9165": 1, # How switch builds MAC address table.
        "CAD350ED-98DB-4C65-AC27-7326DA0D5CE9": 3, # Accurate statements about ICMP ping messages (Ethernet/IP headers).
        "5466F35A-852B-47E8-BD83-C859115F6AE7": 1, # Switch actions when learning source MAC address.
        "D1C4CCAD-E4D4-4BC2-9A68-D5E2A59652A7": 1, # Information held in MAC address table.
        "5CADC56B-CB68-4EDA-B645-0FED436D00B7": 2, # Resulting speed and duplex with autonegotiation.
        "35A3C2FD-786A-4C9B-A1C9-12E522249F1E": 1, # Interpreting `show interfaces` output for manual speed/duplex.
        "F2714D3C-5FA9-4EE4-B16A-17263E343FD9": 2, # Interpreting `show interfaces status` for speed/duplex with power/cable issues.
        "EF6CD19C-6D9C-40D8-8D3E-32154E8C7CAE": 2, # Switch behavior when one end disables autonegotiation.
        "860DA293-D040-47F7-94E5-643A7F364633": 1, # Command for administratively down interface.
        "3397B78A-BAD0-4222-B418-AABFB4FB9C40": 2, # STP behavior with disabled autonegotiation and default settings.
        "6637DEC2-51FE-4DF8-B705-401F8E0C350C": 1, # Common LAN Layer 1 problem indicators.
        "591CE1B8-7426-44D2-8F76-A2364FC0F395": 2, # Interpreting `show interfaces status` for speed/duplex with power/cable issues.
        "58326866-5B87-4694-9A99-BF2B913C7E49": 1, # Resulting speed and duplex with autonegotiation.
        "599352C1-83AE-4E01-BD8F-DE06C168206F": 1, # Resulting speed and duplex with autonegotiation.
        "41A2D253-37DD-4886-A7D0-029019BB7C88": 1, # Command to display allowed VLANs on trunk.
        "D633799C-37C2-4142-A35B-08D482BB7321": 1, # Layer 2 frames forwarded to all other ports in same VLAN.
        "BFE53776-1CC1-4DD2-B2F1-0BBCC4079AEA": 2, # Command to force active trunk negotiation.
        "DD83584C-8ED3-4FB8-9FD4-0E40DCC1DC5A": 2, # Troubleshooting VLAN disabled status.
        "D91D7E7F-B5B7-4695-879B-13DB1D12441A": 2, # Command to administratively disable trunking.
        "68ADB9EC-975C-417F-8CCA-193972040C73": 2, # Interpreting `show vlan brief` output for trunking interfaces.
        "E0E04261-B943-4C9F-9082-2A3807CEEB21": 1, # Characteristics of 802.1Q.
        "93A16F23-A03B-41B9-876E-2D04879D65ED": 2, # Identifying incorrect configuration for voice VLANs.
        "A20994B3-8A22-48DC-8E98-363E78E892F0": 2, # Identifying incorrect configuration for voice VLANs.
        "BAF49872-ADDC-4479-AE5A-390DE0419F78": 2, # Accurate switchport mode combinations for trunking.
        "C0075794-A2C5-426B-A4CD-45B9D9F2C44F": 1, # True statement about native VLAN in ISL and 802.1Q.
        "DFBAAD04-D6BA-4D16-8FAE-498DCA22A9D5": 2, # Interpreting `show interfaces status` output for VLAN column.
        "ABD30171-F813-410B-A1D8-67EE46052AB2": 2, # Correctly stating whether an interface will use trunking based on DTP.
        "B71E7334-FAA1-4BA4-9A54-71355FF59F47": 2, # Interpreting `show vlan brief` and `show version` for trunking interfaces.
        "5347E238-F376-4E0C-9182-842C6C440708": 1, # True statement about `switchport nonegotiate`.
        "679C4805-D9D6-4FBD-994C-C0786707D47C": 2, # True statements about a trunk from `show interfaces trunk` output.
        "6703E3A1-B53C-45F0-B928-D920FD91813D": 2, # Results of changing native VLAN on a trunk.
        "25C4C2FB-CDBF-4FFE-A7C4-DCA7D4AE0916": 1, # Single interface subcommand to stop dynamic trunking.
        "D8FCDDD5-740F-4910-96E0-EAF7195F6107": 1, # Command to configure access port VLAN.
        "3A2D74E7-B069-4E10-9FA5-00E37990E55D": 1, # Potential issues with redundant Layer 2 network without STP.
        "A890CC2E-2DE4-4B17-A279-0DD0804B33E5": 1, # Methods to remove need for spanning tree.
        "C9788CAB-6177-4430-ACEB-15A217A1992F": 1, # Layer of campus network utilizing BPDU Filter.
        "18BD7505-910D-46FA-967F-18E99DD92466": 1, # Functions provided by Spanning Tree Protocol.
        "8070B27A-9F93-48B8-9135-21369F494994": 2, # True statements about STP behavior after stabilization.
        "075C16C2-124F-48A0-AC3C-362E1E1088EE": 3, # True statements about STP behavior with non-default port cost.
        "F8F9709B-A637-4F88-B29B-4544637658D3": 1, # Switch always having a root port.
        "F9F6B47E-5C88-4A81-84AE-4ED6E1752BC2": 1, # Cisco feature detecting switches on PortFast links.
        "8F7E0BDE-D7B5-42D3-A734-5EDB82760892": 2, # Calculating root cost in STP.
        "CEB0AF6B-F2E0-4E47-82CD-831A107E552B": 2, # True statements about STP on a switch with varying root costs.
        "F23FA68B-811F-4CD4-BF3C-85BE37063604": 2, # Determining root port and root cost in STP.
        "6AA893F4-AA62-43C1-A6C0-866828090AC6": 1, # Correct order for spanning-tree algorithm steps.
        "67241FB7-77DB-47D0-B265-980DFA471A58": 1, # Term for total cost between device and root in STP.
        "E7AC1DBC-7BF1-44A4-97DF-9FA73FE6EFE5": 1, # Feature of RSTP not in STP.
        "33D7DC06-AFDC-4D65-B1F3-AD2D6C5D1D29": 1, # RSTP port state replacing disabled/blocking.
        "FED992F1-9540-4F55-8A37-AEE56373783A": 2, # True statements about STP convergence after root change.
        "7A1BB969-577B-4A15-9977-B0F6D7597674": 2, # True statements about RSTP states and roles.
        "A42C33D7-7CC6-49FE-8168-B1EC3562D0CB": 1, # RSTP port states not used by STP.
        "11D32467-B3A4-4BA9-BF9D-B545B9013C13": 1, # Primary decision point for designated port.
        "282ACE53-11C6-4C80-99E3-C246A0F8C1AD": 1, # Port types benefiting from BPDU Guard.
        "0AF1F48A-7CD2-4D4E-8CD2-C937058F1093": 1, # Purpose of Root Guard.
        "459E79F8-ABA4-48B3-BD19-D1F8471FA27F": 2, # RSTP port roles in a given topology.
        "EEAE8A71-BF0D-4C8B-9817-1DF5C6E2C418": 2, # Which switch will become root after failure.
        "517157DB-6678-4017-B307-1F68694E6AEC": 1, # PAgP channel-group modes.
        "14950F61-6F63-4F4A-9F2E-2720F8A33D52": 1, # Cisco proprietary spanning-tree modes.
        "1C3EF86F-D48D-44AB-B12D-5388EF5EECA5": 1, # LACP modes for EtherChannel.
        "21090482-A271-4157-917A-54474347E697": 2, # True statements from `show spanning-tree` output.
        "F2EBDBF0-3DD5-4BCB-AA66-8E4FDF471D9D": 1, # True statements about EtherChannel.
        "F9DC22D1-0DD5-437C-AFF5-92CC26F59917": 2, # True statements about `show etherchannel port-channel` output.
        "D9926A26-2140-4DA8-9CD2-B0EEF0FCF9F4": 1, # IEEE standard spanning-tree modes.
        "FC048DD5-EE06-441B-9C62-BD59AE18EC67": 1, # Settings to configure identically for EtherChannel.
        "A18CED46-E292-4C85-AB90-BE4D5FB70268": 1, # EtherChannel command using Cisco proprietary dynamic protocol.
        "EC20CE4D-B886-4F86-B998-BFDF9A37532D": 2, # True statements about `show spanning-tree` output (RSTP, default costs).
        "991178A4-832C-46B5-B15F-C02EBC29E41A": 1, # PAgP channel-group modes.
        "FD9A65B7-08EC-417A-8BD8-EF5504D9DEA2": 1, # `spanning-tree vlan X root primary` priority choice.
        "3445B3F7-8400-4CC2-9120-F69B7B0E1DA6": 2, # EtherChannel configuration settings causing problems.
        "6B4248A9-F0C2-42E8-AA3E-FC4EA6B81AA4": 2, # True statements about `show etherchannel port-channel` output.
        "c07-ex-0018": 1, # Issue with network (broadcast storm due to no STP).
        "c07-ex-0019": 1, # Command to show MAC address table entry count.
        "c07-ex-0020": 1, # What switch uses for forwarding decision.
        "c07-ex-0021": 1, # Conclusion about computer with specific MAC address.
        "c07-ex-0022": 1, # Switchport type stripping VLAN information.
        "c07-ex-0023": 1, # Correct statement about `show interfaces trunk` output.
        "c07-ex-0029": 1, # Conclusion from `show etherchannel` output (no control protocol).
        "c07-ex-0030": 1, # Mode to configure on other switch for EtherChannel.
        "c07-ex-0031": 1, # Problem with EtherChannel not forming (passive mode).
        "c07-ex-0032": 1, # Which interfaces become root ports in RSTP.
        "c07-ex-0033": 1, # 802.1w switchport state that always forwards traffic.
        "c07-ex-0034": 1, # Command to quickly configure all access ports in PortFast.
        "c07-ex-0035": 1, # AP mode for RF analysis.
        "c07-ex-0036": 1, # AP feature for wired connectivity in warehouse.
        "c07-ex-0037": 1, # EtherChannel mode for link aggregation group.
        "c07-ex-0093": 1, # Cisco tool for network mapping.
        "c08-ex-0019": 1, # Command to reset MAC address table.
        "c08-ex-0020": 1, # What switch uses for forwarding decision.
        "c08-ex-0021": 1, # Conclusion about computer with specific MAC address.
        "c08-ex-0022": 1, # Switchport type stripping VLAN information.
        "c08-ex-0023": 1, # Correct statement about `show interfaces trunk` output.
        "c08-ex-0029": 1, # Conclusion from `show etherchannel` output (no control protocol).
        "c08-ex-0030": 1, # Mode to configure on other switch for EtherChannel.
        "c08-ex-0031": 1, # Problem with EtherChannel not forming (passive mode).
        "c08-ex-0032": 1, # Command to quickly configure all access ports in PortFast.
        "c08-ex-0033": 1, # Conclusion from `show spanning-tree` output (designated mode).
        "c08-ex-0034": 1, # Cause of err-disabled state with BPDU Guard.
        "c08-ex-0035": 1, # AP mode requiring central switching at WLC.
        "c08-ex-0036": 1, # AP mode supporting location-based services but not serving clients.
        "c08-ex-0037": 1, # EtherChannel mode for link aggregation group.
        "45": 1, # Switch forwarding behavior with empty MAC table.
        "7A882A80-AC7E-48C5-A92A-1A002CA143C9": 1, # EtherChannel interface settings that must match.
        "81AB9A42-9AE3-46D9-BA02-DCDC6BA559FB": 1, # Impact on STP when using EtherChannel.
        "B60734C3-3035-4D8A-BDEE-F7E8BD250B80": 1, # Purpose of Loop Guard.
        "jit-b-32": 1, # Frames flooded by a switch.
        "jit-b-51": 1, # Speed and duplex settings with default autonegotiation.
        "jit-b-53": 1, # Result of speed mismatch.
        "jit-b-54": 1, # Error counters incremented on half-duplex device with duplex mismatch.
        "jit-b-78": 1, # True statement about VLANs.
        "jit-b-79": 1, # Result of assigning port to non-existent VLAN.
        "jit-b-80": 1, # Default and undeletable VLANs.
        "jit-b-81": 1, # Untagged VLAN on a trunk port.
        "jit-b-82": 1, # Total number of VLANs.
        "jit-b-83": 1, # VLANs allowed on trunk by default.
        "jit-b-84": 1, # Command to add VLAN to allowed VLANs on trunk.
        "jit-b-85": 1, # Security best practice for native VLAN.
        "jit-b-88": 1, # Operational mode of default connected Cisco switches.
        "jit-b-89": 1, # Switchport mode combinations resulting in valid trunk.
        "jit-b-90": 1, # Administrative modes not sending DTP frames.
        "jit-b-91": 1, # VTP modes syncing VLAN database.
        "jit-b-92": 1, # Switch behavior without VTP domain name.
        "jit-b-93": 1, # VTPv3 modes allowing VLAN creation/propagation.
        "jit-b-94": 1, # VTP versions supporting extended-range VLANs.
        "jit-b-95": 1, # Ports switches send VTP messages out of.
        "jit-b-96": 1, # Negative effects of Layer-2 loops.
        "jit-b-97": 1, # STP root bridge selection.
        "jit-b-98": 1, # Number of root ports in a four-switch LAN.
        "jit-b-99": 1, # STP port roles sending BPDUs.
        "jit-b-100": 1, # Time for PortFast-disabled port to enter forwarding.
        "jit-b-101": 1, # What happens when BPDU Guard-enabled port receives BPDU.
        "jit-b-102": 1, # SW1 root port selection.
        "jit-b-103": 1, # How switches determine designated/non-designated port with equal root costs.
        "jit-b-104": 1, # Number of STP designated ports.
        "jit-b-105": 1, # STP port role pointing away from root and forwarding.
        "jit-b-106": 1, # Command to ensure switch becomes root bridge.
        "jit-b-107": 1, # STP version running when `protocol ieee` is displayed.
        "jit-b-108": 1, # Default port costs with `spanning-tree pathcost method long`.
        "jit-bk-2-109": 1, # Time for port to transition from discarding to forwarding in RSTP.
        "jit-b-110": 1, # RSTP port role (alternate).
        "jit-b-111": 1, # RSTP port type not triggering topology change.
        "jit-b-112": 1, # RSTP port role for root bridge with multiple ports to same segment.
        "jit-b-113": 1, # Command to configure RSTP edge link type.
        "jit-b-114": 1, # How long SW1 waits before reacting to no BPDUs.
        "jit-b-115": 1, # Default RSTP link type on full-duplex ports.
        "jit-b-116": 1, # Number of each RSTP port role in a four-switch LAN.
        "jit-b-117": 1, # Optional STP feature disabling port if it stops receiving BPDUs.
        "jit-b-118": 1, # What happens when BPDU Filter-enabled port receives BPDU.
        "jit-b-119": 1, # False statement about EtherChannel.
        "jit-b-120": 1, # Dynamic EtherChannel mode combinations for valid EtherChannel.
        "jit-b-121": 1, # Setting not needing to match among EtherChannel member ports.
        "jit-b-122": 1, # Dynamic EtherChannel modes forming valid EtherChannel with `mode on`.
        "jit-b-123": 1, # Protocol for negotiating EtherChannel with non-Cisco switch.
        "jit-b-124": 1, # What happens after configuring `switchport mode trunk` on port-channel interface.
        "itn-p-6": 1, # Methods for wireless NIC to discover AP.
        "itn-p-11": 1, # Switch behavior when MAC address table is full.
        "itn-p-15": 1, # Frame forwarding when MAC address table is empty.
        "itn-p-16": 1, # Switch characteristics alleviating network congestion.
        "itn-p-22": 1, # Cisco enhancement of RSTP.
        "itn-p-23": 1, # Advantage of PVST+.
        "itn-p-33": 1, # Command to start EtherChannel group.
        "itn-p-34": 1, # Status of EtherChannel from `show etherchannel summary`.
        "itn-p-35": 1, # Command to correct native VLAN mismatch.
        "itn-p-36": 1, # Traffic type for native VLAN.
        "itn-p-37": 1, # Problem when VLAN not allowed on trunk.
        "itn-p-38": 1, # DTP mode for active trunk negotiation.
        "itn-p-39": 1, # Type of VLAN for network management traffic.
        "itn-p-42": 1, # Command for EtherChannel troubleshooting.
        "itn-p-50": 1, # Potential issue when upgrading AP firmware via WLC.
        "itn-p-51": 1, # Possible cause for SSID not being seen.
        "itn-p-55": 1, # Components of Bridge ID.
        "itn-pr-ex-ccna-002": 1, # Characteristics of 2.4GHz channels.
        "itn-pr-ex-ccna-050": 1, # STP designated ports election.
        "itn-pr-ex-ccna-051": 1, # Port to be assigned with native VLAN.
        "itn-pr-ex-ccna-052": 1, # Purpose of setting native VLAN separate from data VLANs.
        "itn-pr-ex-ccna-053": 1, # Characteristic of EtherChannel.
        "itn-pr-ex-ccna-054": 1, # How data or voice VLANs are configured.
        "itn-pr-ex-ccna-055": 1, # Load-balancing methods in EtherChannel.
        "itn-pr-ex-ccna-058": 1, # Criteria for root bridge election when no priority is configured.
        "itn-pr-ex-ccna-069": 1, # Category of home wireless router.
        "itn-pr-ex-ccna-070": 1, # Feature or function AP provides in wireless LAN.
        "itn-pr-ex-ccna-085": 1, # Protocol implemented to group physical ports.
        "itn-pr-ex-ccna-099": 1, # Protocol supporting port bundle between WLC and switch.
        "itn-pr-ex-ccna-100": 1, # Configurations for switch ports connected to WLC.
        "itn-pr-ex-ccna-101": 1, # Benefit of PortFast.
        "itn-pr-ex-ccna-104": 1, # Difference between autonomous and controller-based APs.
        "itn-pr-ex-ccna-109": 1, # Choice for new wireless device for interoperability.
        "itn-pr-ex-ccna-112": 1, # Functions FlexConnect APs can perform in standalone mode.
        "itn-pr-ex-ccna-119": 1, # Why interfaces are missing from `show vlan brief` output.
        "itn-pr-ex-ccna-121": 1, # 802.11 WLAN standards operating in both 2.4 GHz and 5 GHz.
        "jit-bk-2-156": 1, # Kind of service set with multiple APs.
        "jit-bk-2-157": 1, # Frequency bands with many non-overlapping channels.
        "jit-bk-2-158": 1, # 2.4 GHz channel pattern to avoid interference.
        "jit-bk-2-159": 1, # Uniquely identifies each AP in an ESS.
        "jit-bk-2-160": 1, # 802.11 standards with many non-overlapping channels.
        "jit-bk-2-161": 1, # Identifier as AP's radio MAC address.
        "jit-bk-2-162": 1, # AP mode functioning as wireless client.
        "jit-bk-2-163": 1, # 802.11 standards supporting both 2.4 GHz and 5 GHz bands.
        "jit-bk-2-164": 1, # Wireless LAN's non-unique, human-readable name.
        "jit-bk-2-165": 1, # AP type in MBSS connecting to DS.
        "jit-bk-2-166": 1, # RA of frame when wireless client sends to another client.
        "jit-bk-2-167": 1, # Messages used in passive scanning.
        "jit-bk-2-169": 1, # Kind of AP managed by WLC.
        "jit-bk-2-170": 1, # LWAP mode typically connecting to DS via access link.
        "jit-bk-2-171": 1, # LWAP mode capturing 802.11 frames for analysis.
        "jit-bk-2-172": 1, # Device responsible for switching traffic when FlexConnect local switching is enabled.
        "jit-bk-2-173": 1, # LWAP mode dedicated to analyzing wired LAN traffic.
        "jit-bk-2-174": 1, # Traffic tunneled to Meraki cloud.
        "jit-bk-2-175": 1, # WLC deployment option using dedicated hardware appliance.
        "jit-bk-2-176": 1, # Functions centrally controlled in split-MAC architecture.
        "jit-bk-2-177": 1, # True statement about CAPWAP.
        "jit-bk-2-189": 1, # Methods to connect to GUI of Cisco WLC.
        "jit-bk-2-190": 1, # WLC port type for user data traffic.
        "jit-bk-2-191": 1, # WLC port type for OOB management.
        "jit-bk-2-192": 1, # WLC interface type for CAPWAP tunnels.
        "jit-bk-2-193": 1, # WLC interface type for OOB management.
        "jit-bk-2-194": 1, # Advanced WLAN feature encouraging clients to less-busy LWAPs.
        "jit-bk-2-195": 1, # Hexadecimal WPA2 PSK character count.
        "jit-bk-2-197": 1, # Advanced WLAN feature delaying 2.4 GHz probes.
        "jit-bk-2-199": 1, # WLC interface type for mapping WLANs to VLANs.
        "jit-bk-2-200": 1, # Cisco WLC GUI tab for LWAP settings.
        "jit-bk-2-201": 1, # Ports included in LAG on Cisco WLC.
        "ccnap-008": 1, # Switchport for Accounting VLAN.
        "ccnap-010": 1, # STP root bridge placement for VLANs.
        "ccnap-015": 1, # STP designated ports.
        "ccnap-018": 1, # STP root bridge election.
        "ccnap-030": 1, # VLAN Trunking Protocol (VTP) pruning feature.
        "ccnap-043": 1, # EtherChannel group configuration from output.
        "ccnap-044": 1, # Parameter that can be different on EtherChannel ports.
        "ccnap-045": 1, # EtherChannel configuration for forming link.
        "ccnap-046": 1, # Troubleshooting EtherChannel (duplex mismatch).
        "ccnap-047": 1, # Problem with VLAN communication (no trunk).
        "ccnap-049": 1, # Native VLAN mismatch scenario.
        "ccnap-050": 1, # STP root bridge election with default priority.
        "ccnap-051": 2, # Interpreting MAC address table and CDP output.
        "ccnap-052": 1, # Correct statements regarding RSTP.
        "ccnap-053": 1, # Possible trunking modes for switch port.
        "ccnap-054": 1, # Term describing spanning-tree network with all ports in blocking/forwarding.
        "ccnap-055": 1, # Alternative port selection in STP.
        "ccnap-056": 2, # Interpreting `show spanning-tree` output (root bridge, priority, port states).
        "ccnap-057": 1, # Correct statements regarding 802.1Q trunking.
        "ccnap-059": 1, # Valid modes for switch port as VLAN trunk.
        "ccnap-060": 1, # Benefit of PVST+.
        "ccnap-061": 1, # Spanning-tree designated port role.
        "ccnap-063": 2, # STP port roles and states in a given topology.
        "ccnap-064": 1, # Characteristics of 802.1Q protocol.
        "ccnap-066": 1, # Problem solved by STP.
        "ccnap-068": 1, # Benefits of creating VLANs.
        "ccnap-069": 1, # Interpreting `show spanning-tree` output (not root bridge).
        "ccnap-072": 1, # True statements about RSTP.
        "ccnap-073": 1, # Cause of frame being received on different VLAN.
        "ccnap-074": 1, # Correct configuration for trunk link.
        "ccnap-075": 2, # Spanning-tree designated ports selection.
        "ccnap-076": 1, # VLAN range that can be added/modified/removed.
        "ccnap-077": 1, # Link protocols for carrying multiple VLANs.
        "ccnap-078": 1, # Reason why switch is not root bridge.
        "ccnap-080": 1, # Reason for blocked port in STP.
        "ccnap-082": 1, # Problem with inter-VLAN communication (no trunk).
        "ccnap-083": 1, # Command to enable RSTP.
        "ccnap-084": 1, # Commands to verify trunk link configuration.
        "ccnap-085": 1, # RSTP converged port states.
        "ccnap-087": 1, # Benefits of VLANs.
        "ccnap-088": 1, # IEEE standard protocol initiated by DTP.
        "ccnap-089": 1, # Effect of adding switch ports to new VLAN.
        "ccnap-090": 1, # STP root bridge selection.
        "ccnap-091": 1, # Protocols for preventing Layer 2 loops.
        "ccnap-092": 1, # Function of `switchport trunk native vlan`.
        "ccnap-094": 1, # IEEE 802.1Q standard description.
        "ccnap-095": 1, # Result of setting access VLAN for non-existent VLAN.
        "ccnap-096": 1, # Port state introduced by Rapid-PVST.
        "ccnap-259": 1, # Troubleshooting EtherChannel (speed mismatch).
        "ccnap-266": 1, # Circumstance for multiple copies of unicast frame.
        "ccnap-270": 1, # Result of link failure in STP.
        "r-ccnaq-001": 1, # Necessary configurations for VLANs to span multiple switches.
        "r-ccnaq-007": 1, # Command to enable PortFast.
        "r-ccnaq-010": 1, # Protocols for negotiating EtherChannel.
        "r-ccnaq-027": 1, # Correct statements about RSTP features.
        "r-ccnaq-028": 1, # Correct statements about WLANs.
        "r-ccnaq-030": 1, # Most likely cause for VLAN communication failure.
        "r-ccnaq-035": 1, # Definition of STP convergence.
        "r-ccnaq-054": 1, # Command to display VLAN configuration.
        "r-ccnaq-058": 1, # VTP definition and purpose.
        "r-ccnaq-065": 1, # Primary purpose of EtherChannel.
        "r-ccnaq-068": 1, # Most commonly used VLAN tagging method.
        "r-ccnaq-075": 1, # Correct statements about VLANs and trunking.
        "r-ccnaq-083": 1, # Correct statements about wireless channel interference.
        "r-ccnaq-086": 1, # Command to display trunking information.
        "r-ccnaq-087": 1, # Load-balancing method for Cisco EtherChannel.
        "r-ccnaq-096": 1, # Command to create and enter VLAN configuration mode.
        "itn-14-16-38": 1, # What R1 uses as destination MAC.
        "itn-2-1-4-02": 1, # First action in switch boot sequence.
        "itn-2-1-4-05": 1, # Command for auto-MDIX setting.
        "itn-2-1-4-07": 1, # Command to set BOOT environment variable.
        "itn-2-1-4-08": 1, # What switch uses to locate and load IOS image.
        "itn-2-1-4-12": 1, # After which step boot loader is executed.
        "itn-2-1-4-13": 1, # Impact of adding Layer 2 switch.
        "itn-2-1-4-14": 1, # Characteristic of cut-through switching.
        "itn-2-1-4-15": 1, # Difference between hub and Layer 2 LAN switch.
        "itn-2-1-4-16": 1, # Correct statement about Ethernet switch frame forwarding.
        "itn-2-1-4-17": 1, # How switch buffers affect network performance.
        "itn-2-1-4-18": 1, # Switch characteristic for keeping traffic local.
        "itn-2-1-4-19": 1, # Switch component reducing packet handling time.
        "itn-2-1-4-20": 1, # Information added to switch table from incoming frames.
        "itn-2-1-4-21": 1, # Switching method ensuring error-free frame before forwarding.
        "itn-2-1-4-22": 1, # Number of broadcast domains displayed.
        "itn-2-1-4-23": 1, # Occasions to disable DTP.
        "itn-2-1-4-24": 1, # Characteristics describing native VLAN.
        "itn-2-1-4-25": 1, # Command to remove only VLAN 100.
        "itn-2-1-4-26": 1, # Why interfaces are missing from `show vlan brief` output.
        "itn-2-1-4-27": 1, # What happens when device in VLAN 20 sends broadcast.
        "itn-2-1-4-28": 1, # Remedy for workstations not sending traffic on trunk.
        "itn-2-1-4-29": 1, # What happens to switch ports after VLAN is deleted.
        "itn-2-1-4-30": 1, # Switch mode for router-on-a-stick.
        "itn-2-1-4-31": 1, # What happens when `no switchport access vlan` is entered.
        "itn-2-1-4-32": 1, # Command displaying encapsulation type, voice VLAN ID, access mode VLAN.
        "itn-2-1-4-33": 1, # What is wrong with voice VLAN configuration.
        "itn-2-1-4-34": 1, # Steps to configure voice VLAN.
        "itn-2-1-4-35": 1, # Conclusion from `show interfaces trunk` output.
        "itn-2-1-4-45": 1, # Characteristic of routed port on Layer 3 switch.
        "itn-2-1-4-47": 1, # Effect of `mdix auto` command.
        "itn-2-1-4-48": 1, # Effect of `ip address` command on 2960 switch.
        "itn-2-1-4-49": 1, # Effect of `configure terminal` command.
        "itn-2-1-4-50": 1, # Effect of `shutdown` command.
        "itn-2-1-4-51": 1, # Effect of `ipv6 address` command on 2960 switch.
        "itn-2-1-4-52": 1, # Effect of `exit` command.
        "itn-2-1-4-53": 1, # Effect of `enable` command.
        "itn-2-1-4-54": 1, # Effect of `duplex full` command.
        "itn-2-1-4-55": 1, # VLAN type not carrying voice and network management traffic.
        "itn-2-1-4-56": 1, # VLAN type reserving bandwidth for IP Phone quality.
        "itn-2-1-4-57": 1, # VLAN type initially the management VLAN.
        "itn-2-1-4-58": 1, # VLAN type designed to have delay less than 150 ms.
        "itn-2-1-4-59": 1, # VLAN type separating network into user/device groups.
        "itn-2-1-4-60": 1, # VLAN type configured for network management traffic.
        "itn-2-1-4-61": 1, # VLAN type supporting untagged traffic.
        "itn-2-1-4-62": 1, # Command to bring serial interface up.
        "itn-2-1-4-64": 1, # Solution to alleviate network congestion due to collisions.
        "itn-2-1-4-65": 1, # Correct statements regarding SVI inter-VLAN routing.
        "itn-2-1-4-67": 1, # VLAN type for untagged traffic on trunk port.
        "itn-2-1-4-68": 1, # Output of `show vlan brief` command.
        "itn-2-1-4-69": 1  # Message displayed when IP address entered into web browser.
    }

    for q in questions:
        if q["questionId"] in difficulty_updates:
            q["difficulty"] = str(difficulty_updates[q["questionId"]])
        else:
            # Fallback for any question not explicitly in the manual assessment (shouldn't happen with full list)
            print(f"Warning: Question ID {q['questionId']} not found in manual updates. Retaining original difficulty.")
    return questions

def load_json_with_fallback(filename):
    """
    Loads JSON data from a file, attempting UTF-8 first, then windows-1252, then latin-1,
    and finally with errors='ignore'.
    """
    encodings = ['utf-8', 'windows-1252', 'latin-1']
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                return json.load(f)
        except UnicodeDecodeError:
            print(f"Decode failed for {filename} with encoding '{encoding}'. Trying next...")
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from '{filename}' with encoding '{encoding}': {e}")
            return None
    
    # Final fallback: try reading with errors='ignore'
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            print(f"Attempting to load {filename} with utf-8 and errors='ignore'. Data loss may occur.")
            return json.load(f)
    except Exception as e:
        print(f"Critical error: Could not load {filename} even with errors='ignore': {e}")
        return None

def save_json(data, filename):
    """
    Saves data to a JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved updated questions to '{filename}'.")
    except IOError as e:
        print(f"Error saving file '{filename}': {e}")

if __name__ == "__main__":
    input_file = 'NETAC.json' # Assuming the input file is NETAC.json based on the last successful run
    output_file = 'updated_NETAC.json'

    # Load questions
    questions_data = load_json_with_fallback(input_file)

    if questions_data:
        # Set difficulties
        updated_questions = set_difficulty(questions_data)

        # Save updated questions
        save_json(updated_questions, output_file)